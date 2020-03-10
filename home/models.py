from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Privilege(models.Model):
    view_transaction = models.BooleanField()
    create_transaction = models.BooleanField()
    authorize_transaction = models.BooleanField()
    transaction_type = models.CharField(max_length=20)
    issue_check = models.BooleanField()
    fund_transfer = models.BooleanField()
    view_account = models.BooleanField()
    create_account = models.BooleanField()
    modify_account = models.BooleanField()
    close_account = models.BooleanField()
    delete_account = models.BooleanField()
    account_type = models.CharField(max_length=20)
    request_type = models.CharField(max_length=20)
    access_logs = models.BooleanField()
    user_type = models.CharField(max_length=10)

    def __str__(self):
        return self.user_type
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    mobile_number = models.CharField(max_length=10)
    birthdate = models.DateTimeField()
    ssn = models.CharField(max_length=9)
    user_type = models.CharField(max_length=10)
    joining_date = models.DateTimeField()
    privilege_id = models.ForeignKey(Privilege, on_delete=models.CASCADE)

    def __str__(self):
        if self.user:
            return self.user
        else:
            return self.business_name

class Account(models.Model):
    account_type = models.CharField(max_length=20)
    account_balance = models.BigIntegerField()
    creation_date = models.DateTimeField()
    user = models.ForeignKey(UserProfile, related_name="Account_User_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.account_type

class Transaction(models.Model):
    from_account = models.IntegerField()
    to_account = models.IntegerField()
    transaction_value = models.BigIntegerField()
    transaction_date = models.DateTimeField()
    transaction_type = models.CharField(max_length=20)
    transaction_status = models.CharField(max_length=20)
    user = models.ForeignKey(UserProfile, related_name="Transaction_User_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Appointment(models.Model):
    appointment_date = models.DateTimeField()
    appointment_subject = models.TextField()
    appointment_assigned_to = models.IntegerField()
    user = models.ForeignKey(UserProfile, related_name="Appointment_User_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Requests(models.Model):
    request_date = models.DateTimeField()
    request_subject = models.TextField()
    request_assigned_to = models.IntegerField()
    request_type = models.CharField(max_length=20)
    user = models.ForeignKey(UserProfile,related_name="Requests_User_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.user