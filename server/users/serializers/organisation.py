from rest_framework.serializers import ModelSerializer

from users.models import Organisation, OrganisationCategory
from .account import AccountSerializer

class OrganisationCategorySerializer(ModelSerializer):
    class Meta:
        model = OrganisationCategory
        fields = '__all__'

class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep["category"] = OrganisationCategorySerializer(instance.category).data
        rep["creator"] = AccountSerializer(instance.creator).data

        return rep