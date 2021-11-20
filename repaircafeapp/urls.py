from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'repaircafeapp'
urlpatterns = [
    path('request/', views.index, name='request'),
    path('request/<str:token>/', views.edit, name='edit'),
    path('agenda/', views.agenda, name='agenda'),
    path('profile/', views.profile, name='profile'),
] + static('/media/', document_root=settings.MEDIA_ROOT)
