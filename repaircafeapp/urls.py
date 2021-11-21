from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'repaircafeapp'
urlpatterns = [
    path('repair/', views.index, name='index'),
    path('repair/request/', views.request, name='request'),
    path('repair/request/<str:token>/', views.request_edit, name='edit'),
    path('agenda/', views.agenda, name='agenda'),
    path('profile/', views.profile, name='profile'),
] + static('/media/', document_root=settings.MEDIA_ROOT)
