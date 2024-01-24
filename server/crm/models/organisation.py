from django.db import models

from django.contrib.auth import get_user_model

class Organisation(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    creator = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, null=True)

    category = models.ForeignKey(
        'crm.OrganisationCategory', 
        on_delete=models.DO_NOTHING,
        null=True
    )

    def __str__(self):
        return self.name