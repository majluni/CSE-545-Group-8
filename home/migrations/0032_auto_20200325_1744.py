# Generated by Django 3.0.2 on 2020-03-26 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20200325_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='privilege_id',
        ),
        migrations.DeleteModel(
            name='Privilege',
        ),
    ]
