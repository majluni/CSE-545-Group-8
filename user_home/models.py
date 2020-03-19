from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Appointment(models.Model):
    ASSIGNED_TYPE = (
    ('TIER1','TIER1'),
    ('TIER2', 'TIER2'),
    ('TIER3','TIER3'),
    )
    appointment_date = models.DateTimeField()
    appointment_subject = models.TextField()
    appointment_assigned_to = models.CharField(max_length=20,choices=ASSIGNED_TYPE)
    user = models.ForeignKey(User, related_name="Appointment_User_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
