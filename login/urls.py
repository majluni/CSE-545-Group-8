"""Secure_Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

app_name = "login"

urlpatterns = [
    path('', views.login_user, name='login_base'),
    path('block/', views.login_block, name='login_block'),
    path('otp', views.verify_otp, name='verify_otp'),
    #follow path use to forget jassword
    path('forget_password/',auth_views.ForgetPasswordView.as_view(template_name='forget_passwordt.html'),name = 'forget_password'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html.'),name = 'password_reset'),
    path('reset_success/',auth_views.ResetSuccessView.as_view(template_name='reset_success.html.'),name = 'reset_success')
]
