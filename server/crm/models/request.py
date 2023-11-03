from django.db import models

from .resume import Resume 
from .vacancy import Vacancy

class Request(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)