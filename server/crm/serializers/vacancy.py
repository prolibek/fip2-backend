from rest_framework.serializers import ModelSerializer

from crm.models import Vacancy, VacancyRequest, VacancyRequestStatus
from crm.serializers import ManagerSerializer
from users.serializers import AccountSerializer

class VacancyRequestSerializer(ModelSerializer):
    class Meta:
        model = VacancyRequest 
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(VacancyRequestSerializer, self).__init__(*args, **kwargs)

        self.fields['owner'].required = False

class VacancyRequestStatusSerializer(ModelSerializer):
    class Meta:
        model = VacancyRequestStatus
        fields = ('id', 'status', 'approver', 'date_chosed', 'comments', )
    
    def to_representation(self, instance):
        rep = super().to_representation(instance) 

        rep["approver"] = ManagerSerializer(instance.approver).data 

        return rep

class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep["owner"] = AccountSerializer(instance.owner.user).data

        return rep