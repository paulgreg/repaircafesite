from datetime import datetime, timedelta, timezone
from functools import partial
from django.conf import settings


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)


def next_wednesday(d=datetime.now()):
    return next_weekday(d, 2)  # 0 = Monday, 1=Tuesday, 2=Wednesday...


def next_wednesdays():
    last = datetime.now()
    nexts = list()

    for i in range(settings.REPAIRCAFE_MAX_FUTURES_EVENTS):
        next = next_wednesday(last)
        nexts.append(next)
        last = next

    return nexts
