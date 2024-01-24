from django.db import models 

from .manager import Manager

class VacancyRequest(models.Model):
    owner = models.ForeignKey(Manager, on_delete=models.Manager)
    job_title = models.CharField(max_length=255)
    limit = models.IntegerField(null=True)
    data = models.JSONField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class VacancyRequestStatus(models.Model):
    status_choices = (
        (1, 'Pending'),
        (2, 'Approved'),
        (3, 'Declined')
    )
    
    status = models.SmallIntegerField(choices=status_choices)
    request = models.ForeignKey(VacancyRequest, on_delete=models.CASCADE)
    approver = models.ForeignKey(Manager, on_delete=models.CASCADE)
    date_chosed = models.DateTimeField(null=True)
    comments = models.TextField(null=True)