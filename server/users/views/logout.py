from rest_framework import views, status
from rest_framework.response import Response

from django.conf import settings

class LogoutAPIView(views.APIView):
    def post(self, request):

        response = Response()
        
        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
            expires = "Thu, 01 Jan 1970 00:00:00 GMT",
            max_age=0,
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )

        response.data = {
            "detail": "Account was succesfully logged out."
        }

        return response