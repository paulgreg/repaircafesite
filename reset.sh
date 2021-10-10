#!/bin/sh
docker-compose down --volume
docker-compose up -d
sleep 4
python manage.py migrate
python manage.py createsuperuser --username admin --email test@test.com
python manage.py runserver
