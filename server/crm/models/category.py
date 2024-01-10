from django.db import models

class OrganisationCategory(models.Model):
    name = models.CharField(max_length=60)