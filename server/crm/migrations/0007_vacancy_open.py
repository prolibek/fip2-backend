# Generated by Django 4.2.7 on 2024-02-05 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_remove_vacancyrequest_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='open',
            field=models.BooleanField(default=True),
        ),
    ]