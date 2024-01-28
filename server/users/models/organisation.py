from django.db import models
from django.contrib.auth import get_user_model

from django_tenants.models import TenantMixin, DomainMixin

class OrganisationCategory(models.Model):
    name = models.CharField(max_length=60)

class Organisation(TenantMixin):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)
    slug = models.SlugField(unique=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)

    category = models.ForeignKey(
        OrganisationCategory,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass