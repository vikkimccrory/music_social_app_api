from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.post import Post
from ..serializers import PostSerializer

# Create your views here.
class Posts(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = PostSerializer
    def get(self, request):
        """Index request"""
        # Get all the posts:
        # mangos = Post.objects.all()
        # Filter the posts by owner, so you can only see your owned mangos
        posts = Post.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = PostSerializer(posts, many=True).data
        return Response({ 'posts': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['post']['owner'] = request.user.id
        # Serialize/create mango
        post = PostSerializer(data=request.data['post'])
        # If the mango data is valid according to our serializer...
        if post.is_valid():
            # Save the created mango & send a response
            post.save()
            return Response({ 'post': post.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        post = get_object_or_404(Post, pk=pk)
        # Only want to show owned mangos?
        if not request.user.id == post.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this post')

        # Run the data through the serializer so it's formatted
        data = PostSerializer(post).data
        return Response({ 'post': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate mango to delete
        post = get_object_or_404(Post, pk=pk)
        # Check the mango's owner agains the user making this request
        if not request.user.id == post.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this post')
        # Only delete if the user owns the  mango
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        post = get_object_or_404(Post, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == post.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this post')

        # Ensure the owner field is set to the current user's ID
        request.data['post']['owner'] = request.user.id
        # Validate updates with serializer
        data = PostSerializer(post, data=request.data['post'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
