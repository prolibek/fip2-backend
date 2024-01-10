from rest_framework.serializers import ModelSerializer
from crm.models import OrganisationCategory, VacancyCategory

class OrganisationCategorySerializer(ModelSerializer):
    class Meta:
        model = OrganisationCategory
        fields = '__all__'

class VacancyCategorySerializer(ModelSerializer):
    class Meta:
        model = VacancyCategory 
        fields = '__all__'