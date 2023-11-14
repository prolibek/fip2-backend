from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

class Account(AbstractBaseUser, PermissionsMixin):
    HR = 1
    MANAGER = 2
    CANDIDATE = 3
    role_choices = (
        (1, 'HR'),
        (2, 'Manager'),
        (3, 'Candidate')
    )

    email = models.EmailField(unique=True)

    role = models.SmallIntegerField(choices=role_choices)
    
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    avatar = models.ImageField(null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

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
    department = models.ForeignKey('crm.Department', on_delete=models.DO_NOTHING)

class HR(AccountSubmodel):
    pass

class Candidate(AccountSubmodel):
    pass