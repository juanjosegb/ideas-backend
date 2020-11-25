# IDEAS BACKEND

This project was created with Django 3.1.3 and Graphene Django 2.13.0.

## Installation

# Environments

Create two files .django and .postgres inside folder .envs.    
.django contains the SECRET_KEY to encode user passwords, will be similar to:  

`SECRET_KEY="xxxxxxxxxxxxxxx"`  

.postgres contains the connection parameters to Postgres database, will be similar to:

`POSTGRES_DB=db_name`   
`POSTGRES_PASSWORD=db_password`   
`POSTGRES_HOST=db`   
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

