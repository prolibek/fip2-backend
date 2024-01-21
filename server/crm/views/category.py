from rest_framework.viewsets import ModelViewSet

from crm.serializers import VacancyCategorySerializer, OrganisationCategorySerializer

class VacancyCategoryViewSet(ModelViewSet):
    serializer_class =  VacancyCategorySerializer

class OrganisationCategoryViewSet(ModelViewSet):
    serializer_class = OrganisationCategorySerializer