from django.db import models
from django.contrib.auth import get_user_model

from users.models import Permission

class Member(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

class MemberPermissions(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)