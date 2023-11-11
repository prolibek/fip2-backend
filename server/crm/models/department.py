from django.db import models

class Department(models.Model): 
    name = models.CharField(max_length=155)
    parent_department = models.ForeignKey('self', on_delete=models.CASCADE)
    organisation = models.ForeignKey('crm.Organisation', on_delete=models.CASCADE)