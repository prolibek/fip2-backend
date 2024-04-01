from rest_framework import serializers
from crm.models import Member
from users.serializers import AccountSerializer

class MemberSerializer(serializers.ModelSerializer):
    user = AccountSerializer()

    class Meta:
        model = Member
        fields = ['user', 'date_joined']
