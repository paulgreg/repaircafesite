from django.template import loader
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from ..models import *
from ..dateutils import next_wednesdays, next_wednesday
from functools import partial


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'repaircafeapp/notlogged.html', {'url': '%s?next=%s' % (settings.LOGIN_URL, request.path)})

    models = findByUser(request.user)
    return render(request, 'repaircafeapp/index.html', {'models': models})


@transaction.atomic
def request(request):
    if not request.user.is_authenticated:
        return render(request, 'repaircafeapp/notlogged.html', {'url': '%s?next=%s' % (settings.LOGIN_URL, request.path)})

    if not request.user.email or not request.user.first_name or not request.user.last_name or not request.user.profile.phone_text or not request.user.profile.locality_text:
        return render(request, 'repaircafeapp/noprofile.html')

    nextdates = getDatesWithAvailabilities()

    if(areRequestCountFull(nextdates)):
        return render(request, 'repaircafeapp/full.html')

    action = reverse('repaircafeapp:request')
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            return onSuccess(request, form)
        else:
            return render(request, 'repaircafeapp/request.html', {'action': action, 'form': form, 'nextdates': nextdates})

    form = RequestForm()
    return render(request, 'repaircafeapp/request.html', {'action': action, 'form': form, 'nextdates': nextdates})


@transaction.atomic
def request_edit(request, token):
    if not request.user.is_authenticated:
        return render(request, 'repaircafeapp/notlogged.html', {'url': '%s?next=%s' % (settings.LOGIN_URL, request.path)})

    action = reverse('repaircafeapp:edit', kwargs={'token': token})
    nextdates = getDatesWithAvailabilities(token)
    model = findByToken(token)
    if (not model):
        raise Http404('Demande non trouvée')

    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES,
                           instance=model)
        if form.is_valid():
            return onSuccess(request, form)
        else:
            return render(request, 'repaircafeapp/request.html', {'action': action, 'form': form, 'nextdates': nextdates})

    form = RequestForm(instance=model)
    return render(request, 'repaircafeapp/request.html', {'action': action, 'form': form, 'nextdates': nextdates})


def agenda(request):
    events = getNextRequests(next_wednesday())
    return render(request, 'repaircafeapp/agenda.html', {'events': events})


def getIsoDateAndDate(requestCount, date):
    iso = date.date().isoformat()
    count = requestCount.get(iso) or 0
    return {'date': date.date(), 'iso': iso, 'places': settings.REPAIRCAFE_MAX_SEATS - count}


def getDatesWithAvailabilities(token=''):
    requestCount = getRequestCountByDates(token)
    return list(map(partial(getIsoDateAndDate, requestCount), next_wednesdays()))


def onSuccess(request, form):
    form.save()
    if (settings.REPAIRCAFE_SEND_EMAIL):
        url = reverse('repaircafeapp:edit', kwargs={
            'token': form.instance.token_text})
        send_mail(
            settings.REPAIRCAFE_EMAIL_CONFIRMATION_TITLE,
            settings.REPAIRCAFE_EMAIL_CONFIRMATION_MESSAGE.format(
                settings.REPAIRCAFE_HOST, url),
            settings.REPAIRCAFE_EMAIL,
            [settings.REPAIRCAFE_EMAIL, form.instance.email_text],
            fail_silently=False,
        )
    return render(request, 'repaircafeapp/success.html', {'model': form.instance, 'email': settings.REPAIRCAFE_EMAIL})
