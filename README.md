# IDEAS BACKEND

This project was created with Django 3.1.3 and Graphene Django 2.13.0.

## Features

* Register user
* Login user with JWT
* Change user password
* Publish ideas (logged in), ideas can be public, protected or private.
* Edit visibility idea and text.
* Remove your ideas.
* Follower system. Users can follow other ones and approve or deny requests.
* Find users
* Visibility determine what can you see from other users. Protected: Followers, Private: Own user, Public: Everyone.
* Timeline with your own ideas and the followed user ideas.
* Send email notification when some followed user publish ideas.

## Future implementations

* Reset password
* Push notifications

## Installation

# Environments

Create two files .django and .postgres inside folder .envs.    
.django contains the SECRET_KEY to encode user passwords, will be similar to:  

`SECRET_KEY="xxxxxxxxxxxxxxx"`  

.postgres contains the connection parameters to Postgres database, will be similar to:

`POSTGRES_DB=db`  
`POSTGRES_USER=db_user`  
`POSTGRES_PASSWORD=db_password`  
`POSTGRES_HOST=localhost`  
`POSTGRES_PORT=5432`    

# Docker

Just run the following command to install dependencies and database:

`docker-compose build`   
`docker-compose up` 

# Migrations

Finally, perform the database migration:  

`docker-compose exec web python manage.py makemigrations`  
`docker-compose exec web python manage.py migrate`  


# Launch


The main page will be available in your localhost, port 8000.

