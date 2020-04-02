# Generated by Django 3.0.2 on 2020-04-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pending_Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_account', models.IntegerField()),
                ('to_account', models.IntegerField()),
                ('transaction_value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transaction_date', models.DateTimeField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('transaction_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField(default=0)),
                ('field_type', models.CharField(default='Counter', max_length=10)),
            ],
        ),
    ]
