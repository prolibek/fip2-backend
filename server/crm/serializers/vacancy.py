from rest_framework.serializers import ModelSerializer

from crm.models import Vacancy
from .category import VacancyCategorySerializer
from .organisation import OrganisationSerializer
from .manager import ManagerSerializer

class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ('organisation', )

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['owner'] = ManagerSerializer(instance.owner).data
        rep['category'] = VacancyCategorySerializer(instance.category).data

        return rep