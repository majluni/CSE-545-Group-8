# Generated by Django 3.0.2 on 2020-03-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0002_auto_20200319_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_assigned_to',
            field=models.CharField(choices=[('TIER1', 'TIER1'), ('TIER2', 'TIER2'), ('TIER3', 'TIER3')], max_length=20),
        ),
    ]