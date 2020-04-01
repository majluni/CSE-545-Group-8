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

app_name = "internal_user"

urlpatterns = [
    path('initFundDeposit', views.initFundDeposit, name='init-fund-deposit'),
    path('searchCustomer', views.searchCustomer, name='search-customer'),
    path('depositFund', views.depositFund, name='deposit-fund'),
    path('depositTemplate', views.depositTemplate, name='deposit-template'),
    path('initIssueCheque', views.initIssueCheque, name='init-issue-cheque'),
    path('issueChequeTemplate', views.issueChequeTemplate, name='init-issue-cheque'),
    path('issueCheque', views.issueCheque, name='issue-cheque'),
    path('initViewCustomer', views.initViewCustomer, name='init-view-customer'),
    path('viewCustomer', views.viewCustomer, name='view-customer'),
    path('createCustomer', views.createCustomer, name='create-customer'),
    path('initModifyCustomer', views.initModifyCustomer, name='init-modify-customer'),
    path('modifyCustomerTemplate', views.modifyCustomerTemplate, name='modify-customer-template'),
    path('modifyCustomer', views.modifyCustomer, name='modify-customer'),
    path('deleteCustomer', views.deleteCustomer, name='delete-customer'),
    path('viewRequests', views.viewRequests, name='view-requests'),
    path('', views.viewRequests, name='view-requests'),
    path('updateRequest', views.updateRequest, name='update-request')
]
