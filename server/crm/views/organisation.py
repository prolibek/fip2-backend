from rest_framework.viewsets import ModelViewSet

from crm.serializers import OrganisationSerializer, DepartmentSerializer

class OrganisationViewSet(ModelViewSet):
    serializer_class = OrganisationSerializer

class DepartmentViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer