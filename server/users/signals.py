from django.db.models.signals import post_save
from django.dispatch import receiver
from django_tenants.utils import schema_context
from crm.models import Member 
from users.models import UserOrganisationMembership

@receiver(post_save, sender=Member)
def create_user_organisation_membership(sender, instance, created, **kwargs):
    if created:
        with schema_context('public'):
            UserOrganisationMembership.objects.create(
                user=instance.user,
                organisation=instance.organisation
            )