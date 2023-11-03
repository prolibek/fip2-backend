from django.db import models
from django.contrib.auth import get_user_model

from .vacancy import Vacancy

class Resume(models.Model):
    candidate = models.ForeignKey(
        get_user_model(),
        null=True
    )

class ResumeComment(models.Model):
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.DO_NOTHING
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    text = models.TextField()

class ResumeFile(models.Model):
    resume = models.ForeignKey(
        Resume, 
        on_delete=models.CASCADE
    )
    file = models.FileField()