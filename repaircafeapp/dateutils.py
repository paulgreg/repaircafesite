import datetime


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def next_thursday(d=datetime.datetime.now()):
    return next_weekday(d, 3)  # 0 = Monday, 1=Tuesday, 2=Wednesday...


def next_thursdays():
    d = datetime.datetime.now()
    next1 = next_thursday(d)
    next2 = next_thursday(next1)
    next3 = next_thursday(next2)
    return [next1, next2, next3]
