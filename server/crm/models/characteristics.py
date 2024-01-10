from django.db import models

from .resume import Resume

class Characteristics(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)
    data = models.JSONField()
    
    comments = models.TextField()