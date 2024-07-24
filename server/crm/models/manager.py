from django.db import models

from .members import Member

class Manager(models.Model):
    id = models.CharField(max_length=255, primary_key=True) 
    position = models.CharField(max_length=64)
    parent_manager = models.ForeignKey(
        'self', 
        on_delete=models.DO_NOTHING,
        null=True
    )
    department = models.ForeignKey('crm.Department', on_delete=models.DO_NOTHING, null=True)
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.position