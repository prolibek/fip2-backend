from crm.serializers import VacancyRequestSerializer 
from crm.models import VacancyRequest

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

class VacancyRequestViewSet(ModelViewSet):
    serializer_class = VacancyRequestSerializer

    def get_queryset(self):
        return VacancyRequest.objects.filter(owner__organisation=self.kwargs['organisation_id'])
    
    def create(self, request, *args, **kwargs):
        serializer = VacancyRequestSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(organisation_id=kwargs['organisation_id'])
            return Response(serializer.data)
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )