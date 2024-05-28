from django.db import models 

from .resume import Resume

class ExternalSource(models.Model):
    name = models.CharField(max_length=45, null=False)
    url = models.CharField(max_length=256, null=True)

class ResumeExternalInfo(models.Model):
    source = models.ForeignKey(ExternalSource, on_delete=models.DO_NOTHING)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    text = models.TextField(null=True)