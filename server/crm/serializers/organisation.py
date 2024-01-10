from rest_framework.serializers import ModelSerializer

from crm.models import Organisation, Department

from users.serializers import AccountSerializer

from .category import OrganisationCategorySerializer

class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['creator'] = AccountSerializer(instance.creator).data
        rep['category'] = OrganisationCategorySerializer(instance.category).data

        return rep

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
