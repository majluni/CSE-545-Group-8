from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from datetime import datetime
from create_account import forms
from home.models import User,Profile

from .forms import LoginForm
def login_user(request):
    if request.method=='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            userObj = authenticate(username=form.cleaned_data['user_id'], password=form.cleaned_data['password'])
            user_instance=User.objects.get(username=form.cleaned_data['user_id'])
            profile_instance=Profile.objects.get(user=user_instance)
            if userObj is not None and profile_instance.flag==True:
                login(request,userObj)     
                request.session['last_activity'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                return HttpResponseRedirect('/user_home/')
            else:
                return HttpResponse("Login Failed!!")
            #if authorization is successful, redirect to appropriate page
            #return HttpResponseRedirect('/')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

