from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import AccountUserManager
from crm.models import Department

class Account(AbstractBaseUser, AccountUserManager, PermissionsMixin):
    HR = 1
    MANAGER = 2
    CANDIDATE = 3
    role_choices = (
        (1, 'HR'),
        (2, 'Manager'),
        (3, 'Candidate')
    )

    role = models.SmallIntegerField(choices=role_choices)
    
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55)

    avatar = models.ImageField(null=True)

    objects = AccountUserManager()

# Creating an account model entails creating a submodel depending on a selected role
class AccountSubmodel(models.Model):
    user = models.ForeignKey(
        Account, 
        on_delete=models.CASCADE,
        null=True    
    )

class Manager(AccountSubmodel):
    position = models.CharField(max_length=64) 
    parent_manager = models.ForeignKey(
        'self', 
        on_delete=models.DO_NOTHING,
        null=True
    )
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

class HR(AccountSubmodel):
    pass

class Candidate(AccountSubmodel):
    pass