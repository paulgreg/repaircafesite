from django.urls import path

from . import views

app_name = 'repaircafeapp'
urlpatterns = [
    path('request', views.index, name='request'),
]
