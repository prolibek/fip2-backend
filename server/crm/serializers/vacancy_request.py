from rest_framework.serializers import ModelSerializer

from .manager import ManagerSerializer
from crm.models import VacancyRequest

class VacancyRequestSerializer(ModelSerializer):
    class Meta:
        model = VacancyRequest
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['owner'] = ManagerSerializer(instance.owner).data

        return rep