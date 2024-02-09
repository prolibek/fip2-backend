from django.db import models
from django.contrib.auth import get_user_model

from .vacancy import Vacancy

class Resume(models.Model):
    first_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45, null=True)
    middle_name = models.CharField(max_length=45, null=True)
    age = models.SmallIntegerField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=45, null=True)
    text = models.TextField(null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_received = models.DateTimeField(null=True)

class ResumeComment(models.Model):
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.DO_NOTHING
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

class ResumeFile(models.Model):
    resume = models.ForeignKey(
        Resume, 
        on_delete=models.CASCADE
    )
    file = models.FileField()

class Request(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)