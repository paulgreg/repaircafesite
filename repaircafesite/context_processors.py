from django.conf import settings


def add_constants(request):
    return {
        'LANG': settings.LANG,
        'REPAIRCAFE_TITLE': settings.REPAIRCAFE_TITLE,
        'REPAIRCAFE_ROBOTS': settings.REPAIRCAFE_ROBOTS
    }
