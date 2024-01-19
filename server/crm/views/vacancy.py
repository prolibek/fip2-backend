from crm.serializers import VacancySerializer 
from crm.models import Vacancy, Manager

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

class VacancyViewSet(ModelViewSet):
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.filter(organisation=self.kwargs['organisation_id'])
    
    def create(self, request, *args, **kwargs):
        organisation_id = self.kwargs['organisation_id']

        request.data['organisation'] = organisation_id
        serializer = VacancySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )