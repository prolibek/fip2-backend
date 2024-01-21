from django.db import models

from users.models import Account

class Manager(models.Model):
    position = models.CharField(max_length=64)
    parent_manager = models.ForeignKey(
        'self', 
        on_delete=models.DO_NOTHING,
        null=True
    )
    department = models.ForeignKey('crm.Department', on_delete=models.DO_NOTHING, null=True)
    organisation = models.ForeignKey('crm.Organisation', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.position