# Vikki McCrory
# HitMakers
This application allows the user to create, update, index, show, and delete posts. It is meant to be a "songwriters journal" for you to keep all of your song ideas in one place.

### Technologies Used
- Javascript
- React.js
- HTML
- CSS/Sass
- React Bootstrap
- Django
- PostgreSQL
- Axios

### API Routes
| HTTP Method   | URL Path     | Action           | CRUD     |
|:--------------|:-------------|:-----------------|----------|
| GET           | /posts/    | index or list    | `R`ead   |
| GET           | /posts/`:id`  | show or retrieve | `R`ead   |
| POST          | /posts/     | create           | `C`reate |
| PATCH         | /post/`:id` | update           | `U`pdate |
| DELETE         | /posts/`:id`  | removes post       | `D`elete

# Front-End Repo
https://github.com/vikkimccrory/music-social-app-client

# Deployed API Link
https://music-social-app-api.herokuapp.com

# Deployed Client Link
https://vikkimccrory.github.io/music-social-app-client

# Set Up And Installation
Fork, clone, and run `npm install`

# Planning

### ERD
![ERD](https://i.ibb.co/vLZnxQg/0-3.jpg)

### Process and Problem Solving
- For this project, I started building the back-end API using Django. Once that was working, I moved on to the front-end, for which I used React. When I ran into problems, I tested out a variety of possible solutions before submitting issues. I also collaborated with peers to help debug.

### Unsolved Problems For Future Iterations
- For future versions of this app, I want to turn it into a social media platform for songwriters and producers to share their work with peers. I want to also add audio and video uploading capabilities so users can share their works in progress.
