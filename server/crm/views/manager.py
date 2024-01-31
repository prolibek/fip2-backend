from rest_framework.viewsets import ModelViewSet

from crm.serializers import ManagerSerializer
from crm.models import Manager

from crm.permissions import IsTenantMember

class ManagerViewSet(ModelViewSet):
    permission_classes = (IsTenantMember,)
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()