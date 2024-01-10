from django.db import models

class Organisation(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    creator = models.ForeignKey('users.Account', on_delete=models.DO_NOTHING, null=True)

    category = models.ForeignKey(
        'crm.OrganisationCategory', 
        on_delete=models.DO_NOTHING,
        null=True
    )