from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm, TierStatus
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def internal_homepage(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        tier =TierStatus(request.POST)
        if form.is_valid() and profile_form.is_valid() and tier.is_valid():
            user= form.save()
            acc=tier.save(commit=False)
            profile=profile_form.save(commit=False)
            profile.user=user
            acc.user=profile.user
            profile.save()
            acc.save()

            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            return HttpResponseRedirect('/login/')
    else:
        form=ExtendedUserCreationForm()
        profile_form=UserProfileForm()
        tier=TierStatus()

    context={'form' : form, 'profile_form' : profile_form, 'tier' : tier}
    return render(request,'internal_register.html',context)
