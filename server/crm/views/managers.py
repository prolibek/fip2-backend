from users.models import Account

from crm.serializers import ManagerSerializer
from crm.models import Manager

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

class ManagerViewSet(ModelViewSet):
    serializer_class = ManagerSerializer

    def get_queryset(self):
        return Manager.objects.filter(organisation=self.kwargs['organisation_id'])
    
    def create(self, request, *args, **kwargs):
        serializer = ManagerSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(organisation_id=kwargs['organisation_id'])
            return Response(serializer.data)
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )