from django.db import models 

from .members import Member
from .manager import Manager

class VacancyRequest(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    job_title = models.CharField(max_length=255)
    limit = models.IntegerField(null=True)
    public_data = models.JSONField(null=True)
    private_data = models.JSONField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class VacancyRequestStatus(models.Model):
    status_choices = (
        (1, 'Pending'),
        (2, 'Approved'),
        (3, 'Declined')
    )
    
    status = models.SmallIntegerField(choices=status_choices, default=1)
    request = models.ForeignKey(VacancyRequest, on_delete=models.CASCADE)
    approver = models.ForeignKey(Manager, on_delete=models.CASCADE)
    date_chosed = models.DateTimeField(null=True)
    comments = models.TextField(null=True)