# RepairCafeSite

Work in progress about a repair café web site.

Expected features :

  - wiki (via [django-wiki](https://github.com/django-wiki/django-wiki)) for presentation, rules
  - form to register a repair request
  - calendar to show planned reparations
  - admin interface to update or cancel requests


## Installation

    python -m pip install Django
    python -m pip install pymysql
    python -m pip install django_nyt
    python -m pip install django-mptt
    python -m pip install django-sekizai
    python -m pip install sorl-thumbnail
    python -m pip install wiki

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

to explore :

    python manage.py shell


### Database

A MariaDB database via docker is used for developpement.

A `reset.sh` script deletes db volume, recreate migration, superuser and runserver.

## for production

 - update database password
 - update `SECRET_KEY` in settings.py
 - remove `DEBUG` flag in settings.py



