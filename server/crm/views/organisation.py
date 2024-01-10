from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from crm.serializers import OrganisationSerializer, DepartmentSerializer
from crm.models import Department, Organisation

from django.shortcuts import get_object_or_404

class OrganisationViewSet(ModelViewSet):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance)

        departments = instance.department_set.all().values()

        return Response({
            **serializer.data,
            "departments": departments
        })

class DepartmentViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer
    
    def get_queryset(self):
        return Department.objects.filter(organisation=self.kwargs['organisation_id'])
    
    def create(self, request, *args, **kwargs):
        organisation_id = self.kwargs['organisation_id']

        request.data['organisation'] = organisation_id
        serializer = DepartmentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )