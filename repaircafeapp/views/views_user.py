from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from ..models import UserForm, ProfileForm


@transaction.atomic
def profile(request):
    if not request.user.is_authenticated:
        return render(request, 'repaircafeapp/notlogged.html', {'url': '%s?next=%s' % (settings.LOGIN_URL, request.path)})

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Votre profil est sauvegardé !')
            return render(request, 'repaircafeapp/profile.html', {'user_form': user_form, 'profile_form': profile_form})
        else:
            return render(request, 'repaircafeapp/profile.html', {'user_form': user_form, 'profile_form': profile_form})

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'repaircafeapp/profile.html', {'user_form': user_form, 'profile_form': profile_form})
