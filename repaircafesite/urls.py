from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('repaircafe/', include('repaircafeapp.urls')),

    path('_accounts/password_reset/',
         views.PasswordResetView.as_view(), name='password_reset', ),
    path('_accounts/password_reset/done/', views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('_accounts/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('_accounts/reset/done/', views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),


    path('notifications/', include('django_nyt.urls')),
    path('', include('wiki.urls'))
]
