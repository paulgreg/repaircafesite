from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import RequestForm, getRequestCountByDates, getNextRequests, findByToken, areRequestCountFull
from .dateutils import next_thursdays, next_thursday
from functools import partial
from django.conf import settings
from django.urls import reverse


def getIsoDateAndDate(requestCount, date):
    iso = date.date().isoformat()
    count = requestCount.get(iso) or 0
    return {'date': date.date(), 'iso': iso, 'places': settings.REPAIRCAFE_MAX_SEATS - count}


def getDatesWithAvailabilities(token=''):
    requestCount = getRequestCountByDates(token)
    print(requestCount)

    return list(map(partial(getIsoDateAndDate, requestCount), next_thursdays()))


def index(request):
    nextdates = getDatesWithAvailabilities()

    if(areRequestCountFull(nextdates)):
        return render(request, 'repaircafeapp/full.html')

    action = reverse('repaircafeapp:request')
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'repaircafeapp/success.html', {'model': form.instance, 'email': settings.REPAIRCAFE_EMAIL})
        else:
            return render(request, 'repaircafeapp/request.html', {'action': action, 'form': form, 'nextdates': nextdates})

    form = RequestForm()
    # to debug
    form.instance.name_text = 'Dupont'
    form.instance.firstname_text = 'Jacques'
    form.instance.email_text = 'jacques@dupont.fr'
    form.instance.phone_text = '0612345678'
    form.instance.locality_text = 'Paris'
    form.instance.brand_text = 'sony'
    form.instance.model_text = 'STR550'
    form.instance.year_text = '2010'
    form.instance.problem_text = 'mon problème...'
    form.instance.research_text = 'blabla'
    form.instance.actions_text = 'blabla'
    form.instance.expectation_text = 'blabla'
    form.instance.commitment_text = 'blabla'
    return render(request, 'repaircafeapp/request.html', {'action': action, 'form': form, 'nextdates': nextdates})


def edit(request, token):
    action = reverse('repaircafeapp:edit', kwargs={'token': token})
    nextdates = getDatesWithAvailabilities(token)
    model = findByToken(token)
    if (not model):
        raise Http404('Demande non trouvée')

    if request.method == 'POST':
        form = RequestForm(instance=model, data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'repaircafeapp/success.html', {'model': form.instance, 'email': settings.REPAIRCAFE_EMAIL})
        else:
            return render(request, 'repaircafeapp/request.html', {'action': action, 'form': form, 'nextdates': nextdates})

    form = RequestForm(instance=model)
    return render(request, 'repaircafeapp/request.html', {'action': action, 'form': form, 'nextdates': nextdates})


def agenda(request):
    events = getNextRequests(next_thursday())
    return render(request, 'repaircafeapp/agenda.html', {'events': events})
