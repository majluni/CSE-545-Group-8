# Generated by Django 3.0.2 on 2020-03-08 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_transaction_transaction_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.IntegerField()),
                ('mobile_number', models.CharField(max_length=10)),
                ('birthdate', models.DateTimeField()),
                ('ssn', models.CharField(max_length=9)),
                ('user_type', models.CharField(max_length=10)),
                ('joining_date', models.DateTimeField()),
                ('privilege_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Privilege')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Account_User_id', to='home.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Appointment_User_id', to='home.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requests',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Requests_User_id', to='home.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_User_id', to='home.UserProfile'),
            preserve_default=False,
        ),
    ]
