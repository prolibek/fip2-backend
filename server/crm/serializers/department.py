from rest_framework.serializers import ModelSerializer

from crm.models import Department

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'