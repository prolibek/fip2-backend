from rest_framework import serializers

from crm.models import Vacancy

class VacancySerializer(serializers.ModelSerializer):
    model = Vacancy
    fields = '__all__'