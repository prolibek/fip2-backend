from django.conf import settings

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions
from rest_framework.response import Response

def enforse_csrf(request):
    check = CSRFCheck(request)
    check.process_request(request)
    reason = check.process_view(request, None, (), [])
    if reason:
        raise exceptions.PermissionDenied(f'CSRF Denied: {reason}')

class AccountAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None 
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            raw_token = None

        try:
            validated_token = self.get_validated_token(raw_token)
        except:
            return None
        
        enforse_csrf(request)

        return self.get_user(validated_token), validated_token