from django.db import models
from django.contrib.auth import get_user_model

from .manager import Manager

from .organisation import Organisation
from .form import FormField, FormChoiceOptions

class VacancyCategory(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(null=True)
    owner = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    category = models.ForeignKey(
        VacancyCategory, 
        on_delete=models.DO_NOTHING,
        null=True
    )

    def __str__(self):
        return self.title