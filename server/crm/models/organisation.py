from django.db import models

class OrganisationCategory(models.Model):
    name = models.CharField(max_length=60)

class Organisation(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    category = models.ForeignKey(
        OrganisationCategory, 
        on_delete=models.DO_NOTHING
    )