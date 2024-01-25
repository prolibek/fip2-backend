from users.models import Account

from crm.serializers import ManagerSerializer
from crm.models import Manager

from rest_framework.viewsets import ModelViewSet

class ManagerViewSet(ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()