from rest_framework import serializers
from users.models import Account

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    middle_name = serializers.CharField(required=False, allow_blank=True, default='')
    birth_date = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = Account
        fields = ('id', 'email', 'first_name', 'last_name', 'middle_name', 'birth_date', 'role', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
            
        instance.save()
        return instance