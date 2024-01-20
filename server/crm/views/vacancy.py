from crm.serializers import VacancySerializer 
from crm.models import Vacancy, Resume

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from django.shortcuts import get_object_or_404

class VacancyViewSet(ModelViewSet):
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.filter(organisation=self.kwargs['organisation_id'])
    
    def create(self, request, *args, **kwargs):
        serializer = VacancySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(organisation_id=kwargs['organisation_id'])
            return Response(serializer.data)
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )