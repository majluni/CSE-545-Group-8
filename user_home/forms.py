from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home import models

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields=('appointment_date','appointment_subject','appointment_assigned_to',)

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields=('email', 'first_name', 'last_name',)

    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data['email']
        user.username=user.email
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.save()
        return user

class AccountForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields=('account_type',)

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields=('account_type',)


        