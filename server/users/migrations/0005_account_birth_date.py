# Generated by Django 4.2.7 on 2024-03-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_organisation_ceo_alter_organisation_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
