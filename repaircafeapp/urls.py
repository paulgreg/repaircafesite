from django.urls import path
from . import views

app_name = 'repaircafeapp'
urlpatterns = [
    path('request/', views.index, name='request'),
    path('request/<str:token>/', views.edit, name='edit'),
    path('agenda/', views.agenda, name='agenda'),
]
