from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import RequestForm
from .dateutils import next_thursdays


def index(request):
    nextdates = next_thursdays()

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
