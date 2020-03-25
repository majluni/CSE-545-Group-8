from django.urls import path
from . import views

app_name = "internal_homepage"

urlpatterns = [
    path('', views.internal_homepage, name = 'create_internal_account_homepage')
]