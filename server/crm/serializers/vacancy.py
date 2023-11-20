from rest_framework.serializers import ModelSerializer

from crm.models import Vacancy

class VacancySerializer(ModelSerializer):
    model = Vacancy
    fields = '__all__'