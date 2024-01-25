from django.db import models 

class Permission(models.Model):
    description = models.CharField(max_length=255)