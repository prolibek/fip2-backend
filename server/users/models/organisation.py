from django.db import models
from django.contrib.auth import get_user_model

from django_tenants.models import TenantMixin, DomainMixin

class Organisation(TenantMixin):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, unique=True)
    slug = models.SlugField(unique=True)

    ceo = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, null=True, related_name='ceo')
    creator = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, related_name='creator')

    def __str__(self):
        return self.name

class UserOrganisationMembership(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Domain(DomainMixin):
    pass