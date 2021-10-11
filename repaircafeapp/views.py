from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import RequestForm, getRequestCountByDates, getNextRequests
from .dateutils import next_thursdays, next_thursday
from functools import partial
from django.conf import settings


def getIsoDateAndDate(requestCount, date):
    iso = date.date().isoformat()
    count = requestCount.get(iso) or 0
    return {'date': date.date(), 'iso': iso, 'places': settings.MAX_PLACES - count}


def getDatesWithAvailabilities():
    requestCount = getRequestCountByDates()
    print(requestCount)

    nextdates = list(
        map(partial(getIsoDateAndDate, requestCount), next_thursdays()))
    print(nextdates)
    return nextdates


def index(request):
    nextdates = getDatesWithAvailabilities()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'repaircafeapp/success.html', {})
        else:
            return render(request, 'repaircafeapp/request.html', {'form': form, 'nextdates': nextdates})

    form = RequestForm()
    # to debug
    form.name = 'Dupont'
    form.firstname = 'Jacques'
    form.email = 'jacques@dupont.fr'
    form.phone = '0612345678'
    form.locality = 'Paris'
    form.brand = 'sony'
    form.model = 'STR550'
    form.year = '2010'
    form.problem = 'mon problème...'
    form.research = 'blabla'
    form.actions = 'blabla'
    form.expectation = 'blabla'
    form.commitment = 'blabla'
    return render(request, 'repaircafeapp/request.html', {'form': form, 'nextdates': nextdates})


def agenda(request):
    events = getNextRequests(next_thursday())
    return render(request, 'repaircafeapp/agenda.html', {'events': events})
