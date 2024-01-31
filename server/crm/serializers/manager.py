from rest_framework.serializers import ModelSerializer

from crm.models import Manager 

class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'