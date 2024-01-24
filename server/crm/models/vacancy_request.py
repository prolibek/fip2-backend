from django.db import models 

from .manager import Manager

class VacancyRequest(models.Model):
    owner = models.ForeignKey(Manager, on_delete=models.Manager)
    job_title = models.CharField(max_length=255)
    limit = models.IntegerField(null=True)
    data = models.JSONField(null=True)