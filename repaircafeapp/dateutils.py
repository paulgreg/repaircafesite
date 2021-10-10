import datetime
from functools import partial


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def next_thursday(d=datetime.datetime.now()):
    return next_weekday(d, 3)  # 0 = Monday, 1=Tuesday, 2=Wednesday...


def next_thursdays(t=4):
    last = datetime.datetime.now()
    nexts = list()

    for i in range(t):
        next = next_thursday(last)
        nexts.append(next)
        last = next

    return nexts
