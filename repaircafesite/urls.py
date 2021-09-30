from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('repaircafe/', include('repaircafeapp.urls')),
    path('notifications/', include('django_nyt.urls')),
    path('', include('wiki.urls'))
]
