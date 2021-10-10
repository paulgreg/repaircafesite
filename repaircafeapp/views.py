from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import RequestForm


def index(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        print('post')
        print(form.is_valid())
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('./success')
            return render(request, 'repaircafeapp/success.html', {})
        else:
            return render(request, 'repaircafeapp/request.html', {'form': form})

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
    return render(request, 'repaircafeapp/request.html', {'form': form})
