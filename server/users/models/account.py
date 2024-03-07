from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.managers import AccountUserManager

class Account(AbstractBaseUser, PermissionsMixin):
    HR = 1
    MANAGER = 2
    CANDIDATE = 3
    role_choices = (
        (1, 'HR'),
        (2, 'Manager')
    )

    email = models.EmailField(unique=True)

    role = models.SmallIntegerField(choices=role_choices)
    
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, null=True)

    birth_date = models.DateField(null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    avatar = models.ImageField(null=True)

    objects = AccountUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']