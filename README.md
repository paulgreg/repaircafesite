# RepairCafeSite

Work in progress about a repair café web site.

Expected features :

  - wiki (via [django-wiki](https://github.com/django-wiki/django-wiki)) for presentation, rules
  - form to register a repair request
  - calendar to show planned reparations
  - admin interface to update or cancel requests


## Configuration

Copy `repaircafesite/settings.py.dist` to `repaircafesite/settings.py` and change it according your needs.


### for production

 - update database password
 - update `SECRET_KEY` in settings.py
 - remove `DEBUG` flag in settings.py


## Installation

    python -m pip install Django pymysql django_nyt django-mptt django-sekizai sorl-thumbnail wiki

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver


## Development


    docker-compose down --volume
    docker-compose up -d
    python manage.py migrate
    python manage.py createsuperuser --username admin --email test@test.com
    python manage.py runserver

to explore :

    python manage.py shell


### Database

A MariaDB database via docker is used for developpement.