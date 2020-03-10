from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

        
class Profile(models.Model):
    USER_TYPE = (
    ('personal','PERSONAL'),
    ('business', 'BUSINESS'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    mobile_number = models.CharField(max_length=10)
    birthdate = models.DateTimeField()
    ssn = models.CharField(max_length=9)
    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    joining_date = models.DateTimeField(default=datetime.now)
    
    # def __str__(self):
    #     if self.user:
    #         return self.user.first_name
    #     else:
    #         return self.business_name

class Account(models.Model):
    ACCOUNT_TYPE = (
    ('savings','SAVINGS'),
    ('business', 'BUSINESS'),
    ('credit_card','CREDIT_CARD'),
    )
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    account_balance = models.BigIntegerField(default=0)
    creation_date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_type

