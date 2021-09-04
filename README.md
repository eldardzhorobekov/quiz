#Quiz API

### Requirements:

    Docker 20.10.8
    Docker-compose 1.29.2

### Lang & Tech:

    Python 3.9.6
    Django 2.2.10
    djangorestframework 3.12.4
    postgresql 11
    nginx

Server is not configured to run in development mode.

### How to run:
Create .env file in root directory and pass there. You may use different names - this is just the default configuration.

    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    
    SECRET_KEY=<some secret key>
    DEBUG=True
    
    DB_HOST=db
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASS=postgres

Make backend/entrypoint.sh executable

    chmod 777 backend/entrypoint.sh

Make sure that locahost:5000 port is not busy.
Build and run docker-compose  
    
    docker-compose build
    docker-compose up

Open in browser localhost:5000:

    localhost:5000/api - API root
    localhost:5000/admin - Admin page
    localhost:5000/swagger - API docs
    