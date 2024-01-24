from rest_framework.serializers import ModelSerializer

from crm.models import Manager

from users.serializers import AccountSerializer

class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        exclude = ('organisation', )