# Generated by Django 4.2.7 on 2024-02-11 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_vacancy_open'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestStatusResponders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responder', models.SmallIntegerField(choices=[(1, 'HR'), (2, 'Vacancy Owner'), (3, 'CEO'), (4, "Vacancy Owner's Head"), (5, 'Anyone')])),
                ('request_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.requeststatus')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.requeststatus'),
            preserve_default=False,
        ),
    ]
