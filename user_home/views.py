from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import AppointmentForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def user_home(request):
	if request.user.is_authenticated:
		# return HttpResponse('Session established')
		return render(request, 'user_homepage.html', {'username':request.user.username})
	else:
		return HttpResponse('Try again!')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def appointment(request):
    print("yo1")
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print("yo2")
            app=form.save(commit=False)
            app.user=request.user
            app.save()
            username = request.user.username
            password = request.user.password
            app=authenticate(username=username, password=password)
            return HttpResponseRedirect('/user_home/')
    else:
        form=AppointmentForm()
    print("yo3")
    context={'form' : form}
    return render(request,'Appointment/appointment.html',context)