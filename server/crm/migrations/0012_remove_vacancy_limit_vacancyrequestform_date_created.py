# Generated by Django 4.2.7 on 2024-04-23 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_remove_vacancyrequest_ceo_approve_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='limit',
        ),
        migrations.AddField(
            model_name='vacancyrequestform',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 4, 23, 7, 6, 24, 766904, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
