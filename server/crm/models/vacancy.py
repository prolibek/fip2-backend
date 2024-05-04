from django.db import models
from django.contrib.auth import get_user_model

from .members import Member
from .vacancy_request import VacancyRequest

class VacancyCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    job_title = models.CharField(max_length=255)
    owner = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    public_data = models.JSONField(null=True)
    private_data = models.JSONField(null=True)
    public_info = models.TextField(null=True)
    comments = models.TextField(null=True)

    vacancy_request = models.ForeignKey(VacancyRequest, on_delete=models.DO_NOTHING, null=True)

    category = models.ForeignKey(
        VacancyCategory, 
        on_delete=models.DO_NOTHING,
        null=True
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(null=True)

    published = models.BooleanField(default=False)
    open = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title

class VacancyComment(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)