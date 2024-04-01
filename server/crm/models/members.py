from django.db import models 
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

from users.models import Permission, Organisation

class Member(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

class MemberPermissions(models.Model): 
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

class Invitation(models.Model):
    email = models.EmailField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, unique=True)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_string(50)
        super().save(*args, **kwargs)

    def send_invitation(self):
        link = f"{settings.FRONTEND_URL}/join/{self.token}/"
        message = f"Please use this link to join: {link}"
        send_mail(
            'Invitation to Join',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=False,
        )

    @classmethod
    def create_invitation(cls, email, organisation):
        invitation = cls(email=email, organisation=organisation)
        invitation.save()
        invitation.send_invitation()

        return invitation