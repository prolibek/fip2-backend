from rest_framework.serializers import ModelSerializer

from crm.models import Vacancy
from .category import VacancyCategorySerializer
from users.serializers import AccountSerializer

class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['owner'] = AccountSerializer(instance.owner).data
        rep['category'] = VacancyCategorySerializer(instance.category).data

        return rep