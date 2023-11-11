from django.db import models
from django.contrib.auth import get_user_model

from users.models import Manager

from .organisation import Organisation

class VacancyCategory(models.Model):
    name = models.CharField(max_length=60)

class VacancyRequestForm(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

class VacancyRequestField(models.Model):
    form = models.ForeignKey(VacancyRequestForm, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50)

class VacancyRequest(models.Model):
    title = models.CharField(max_length=60)
    data = models.JSONField()

    owner = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)

    status_choices = (
        (1, "ACCEPTED"),
        (2, "DENIED"),
    )
    status = models.SmallIntegerField()

class Vacancy(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    owner = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)

    category = models.ForeignKey(
        VacancyCategory, 
        on_delete=models.DO_NOTHING
    )