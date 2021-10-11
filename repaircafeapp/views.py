from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import RequestForm, getRequestCountByDates
from .dateutils import next_thursdays
from functools import partial
from django.conf import settings


def getIsoDateAndDate(a, d):
    iso = d.date().isoformat()
    count = a.get(iso) or 0
    return {'date': d.date(), 'iso': iso, 'places': settings.MAX_PLACES - count}


def getAvailibility(date):
    return {'iso': date.get('reparation_day_text'), 'count': date.get('count')}


def getDatesWithAvailabilities():
    requestCount = getRequestCountByDates()

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
