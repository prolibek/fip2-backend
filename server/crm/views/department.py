from rest_framework.viewsets import ModelViewSet

from crm.models import Department
from crm.serializers import DepartmentSerializer

class DepartmentViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()