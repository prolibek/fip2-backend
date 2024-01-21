from rest_framework.serializers import ModelSerializer

from crm.models import Manager

from users.serializers import AccountSerializer

class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep["user"] = AccountSerializer(instance.user).data
        
        return rep