from django.db import models
from django.contrib.auth import get_user_model

class OrganisationCategory(models.Model):
    name = models.CharField(max_length=60)

class Organisation(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    ceo = models.ForeignKey(
        get_user_model(),
        null=True
    )
    hr = models.ForeignKey(
        get_user_model(),
        null=True
    )

    category = models.ForeignKey(
        OrganisationCategory, 
        on_delete=models.DO_NOTHING
    )

class Department(models.Model): 
    name = models.CharField(max_length=155)
    parent_department = models.ForeignKey('self', on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)