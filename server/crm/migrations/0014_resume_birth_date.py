# Generated by Django 4.2.7 on 2024-05-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_resume_full_name_vacancycomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
