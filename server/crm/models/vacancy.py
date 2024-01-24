from django.db import models
from django.contrib.auth import get_user_model

from .manager import Manager

class VacancyCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    job_title = models.CharField(max_length=255)
    owner = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    limit = models.IntegerField(null=True)

    category = models.ForeignKey(
        VacancyCategory, 
        on_delete=models.DO_NOTHING,
        null=True
    )

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
