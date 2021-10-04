from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {}
    return render(request, 'repaircafeapp/demand.html', context)


def submit(request):
    context = {}
    return render(request, 'repaircafeapp/demand.html', context)
