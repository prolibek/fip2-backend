# Generated by Django 4.2.7 on 2024-03-10 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_account_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrganisationMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='category',
        ),
        migrations.AlterField(
            model_name='organisation',
            name='description',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='OrganisationCategory',
        ),
        migrations.AddField(
            model_name='userorganisationmembership',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organisation'),
        ),
        migrations.AddField(
            model_name='userorganisationmembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
