from crm.serializers import VacancySerializer 
from crm.models import Vacancy  

from rest_framework.viewsets import ModelViewSet

class VacancyViewSet(ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()