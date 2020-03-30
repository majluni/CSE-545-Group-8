from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import AppointmentForm,UserUpdateForm,AccountForm, AccountDeleteForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.edit import UpdateView
from home import models

# Create your views here.
def user_home(request):      
    profile_instance = models.Profile.objects.get(user=request.user)
    if request.user.is_authenticated and request.user.is_active and profile_instance.privilege_id.user_type=="Customer" and profile_instance.flag==1:
		# return HttpResponse('Session established')
        return render(request, 'user_homepage.html', {'username':request.user.username})
    else:
        return HttpResponse('Try again!')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def appointment(request):
    profile_instance = models.Profile.objects.get(user=request.user)
    if request.user.is_authenticated and request.user.is_active and profile_instance.privilege_id.user_type=="Customer" and profile_instance.flag==1:
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                app=form.save(commit=False)
                app.user=request.user
                app.save()
                return HttpResponseRedirect('/user_home/')
            else:
                return HttpResponse("invalid form")
        else:
            form=AppointmentForm()
        context={'form' : form}
        return render(request,'Appointment/appointment.html',context)
    else:
        return HttpResponse("Login Failed!! Wrong username or password")

def newAccount(request):
    profile_instance = models.Profile.objects.get(user=request.user)
    if request.user.is_authenticated and request.user.is_active and profile_instance.privilege_id.user_type=="Customer" and profile_instance.flag==1:
        if request.method == 'POST':
            acc_form = AccountForm(request.POST)
            if acc_form.is_valid():
                a=acc_form.save(commit=False)
                a.user=request.user
                a.save()
                return HttpResponseRedirect('/user_home/')
            else:
                return HttpResponse("invalid form")
        else:
            acc_form = AccountForm()
        context={'acc_form' : acc_form}
        return render(request,'new_account/new_account.html',context)
    else:
        return HttpResponse("Login Failed!! Wrong username or password")

def deleteAccount(request):
    profile_instance = models.Profile.objects.get(user=request.user)
    if request.user.is_authenticated and request.user.is_active and profile_instance.privilege_id.user_type=="Customer" and profile_instance.flag==1:
        if request.method == 'POST':
            acc_form = AccountDeleteForm(request.POST)
            if acc_form.is_valid():
                acc_number=acc_form.cleaned_data
                account_instance = models.Account.objects.get(account_number=acc_number.get('account_number'))
                account_instance.delete=True
                account_instance.save()
                return HttpResponseRedirect('/user_home/')
            else:
                return HttpResponse("invalid form")
        else:
            acc_form = AccountDeleteForm()
        context={'acc_form' : acc_form}
        return render(request,'delete_account/delete_account.html',context)
    else:
        return HttpResponse("Login Failed!! Wrong username or password")

def updateProfile(request):
    profile_instance = models.Profile.objects.get(user=request.user)
    if request.user.is_authenticated and request.user.is_active and profile_instance.privilege_id.user_type=="Customer" and profile_instance.flag==1:
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST)
            if user_form.is_valid():
                u=user_form.save(commit=False)
                u.user=request.user
                u.save()
                return HttpResponseRedirect('/user_home/')
            else:
                return HttpResponse("invalid form")
        else:
            user_form = UserUpdateForm()
        context={'user_form' : user_form}
        return render(request,'profile_update/profile_update.html',context)
    else:
            return HttpResponse("Login Failed!! Wrong username or password")
