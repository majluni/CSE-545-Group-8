# Generated by Django 3.0.2 on 2020-03-09 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='privilege_id',
        ),
    ]