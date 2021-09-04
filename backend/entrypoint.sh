#!/bin/sh
until cd /usr/src/app/backend/
do
  echo "Waiting for server volume..."
done

. ./env/bin/activate

until ./manage.py migrate
do
  echo "Waiting for database to be ready..."
  sleep 2
done

./manage.py collectstatic --noinput
./manage.py runserver 0.0.0.0:5100
