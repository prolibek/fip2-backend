from rest_framework import serializers
from users.models import Account

from rest_framework_simplejwt.tokens import RefreshToken

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email', 'first_name', 'last_name', 'middle_name', 'role')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)

            if password is not None:
                instance.set_password(password)

            instance.save()

            return instance

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is invalid or expired.')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']

        return attrs
    
    def save(self):
        try: 
            RefreshToken(self.token).blacklist()
        except:
            self.fail('bad_token')