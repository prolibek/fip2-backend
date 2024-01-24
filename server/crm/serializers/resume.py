from rest_framework.serializers import ModelSerializer

from crm.models import Resume
from .vacancy import VacancySerializer

class ResumeSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['vacancy'] = VacancySerializer(instance.vacancy).data

        return rep