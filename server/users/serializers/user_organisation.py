from rest_framework import serializers
from users.models import UserOrganisationMembership
from .organisation import OrganisationSerializer

class UserOrganisationMembershipSerializer(serializers.ModelSerializer):
    organisation = OrganisationSerializer(read_only=True)
    
    class Meta:
        model = UserOrganisationMembership
        fields = '__all__'
