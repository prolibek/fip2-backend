from django.db import models
from django.contrib.auth import get_user_model

from users.models import Manager

from .organisation import Organisation
from .form import FormField, FormChoiceOptions

class VacancyCategory(models.Model):
    name = models.CharField(max_length=60)

class Vacancy(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    owner = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)

    category = models.ForeignKey(
        VacancyCategory, 
        on_delete=models.DO_NOTHING,
        null=True
    )