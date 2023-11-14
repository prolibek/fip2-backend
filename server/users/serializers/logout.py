from rest_framework import serializers
from users.models import Account

from rest_framework_simplejwt.tokens import RefreshToken

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is invalid or expired.')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']

        return attrs
    
    def save(self):
        RefreshToken(self.token).blacklist()