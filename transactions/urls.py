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

app_name = "transactions"

urlpatterns = [
    path('initfundTransfer', views.initfundTransfer, name='init-fund-transfer'),
    path('fundTransfer', views.fundTransfer, name='fund-transfer'),
    path('pendingTransactions', views.pendingTrans, name='pending-transactions'),
    path('updateTransaction', views.updateTransaction, name='update-transaction'),
    path('deposit', views.fund_deposit, name='fund-deposit'),
    path('withdraw', views.fund_withdraw, name='fund-withdraw'),
    path('getStatement', views.generateStatements, name='get-statement'),
    path('redirectToHome', views.redirectToHome, name='get-home'),
]
