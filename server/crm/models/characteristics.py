from django.db import models

from .resume import Resume
from .organisation import Organisation
from .form import FormField, FormChoiceOptions

class CriteriaForm(models.Model):
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

class CriteriaField(FormField):
    form = models.ForeignKey(CriteriaForm, on_delete=models.CASCADE)

class CriteriaChoiceOptions(FormChoiceOptions):
    field = models.ForeignKey(CriteriaField, on_delete=models.CASCADE)

class Characteristics(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    data = models.JSONField()
    
    comments = models.TextField()