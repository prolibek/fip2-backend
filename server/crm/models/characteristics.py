from django.db import models

from .resume import Resume
from .organisation import Organisation

class CriteriaForm(models.Model):
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

class CriteriaField(models.Model):
    form = models.ForeignKey(CriteriaForm, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50)

class CriteriaChoices(models.Model):
    field = models.ForeignKey(CriteriaField, on_delete=models.CASCADE)
    choice_name = models.CharField(max_length=255)

class Characteristics(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    data = models.JSONField()
    comments = models.TextField()