from rest_framework.serializers import ModelSerializer
from crm.models import Organisation, Department

class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
