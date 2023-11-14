from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework import views, status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPIView(views.APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(email=email, password=password)

        if user is None:
            return Response({
                'detail': 'Incorrect email or username'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        response = Response()
        tokens = RefreshToken.for_user(user)

        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE'],
            expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            value = str(tokens.access_token),
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )

        response.data = {
            'access_token': str(tokens.access_token),
            'refresh_token': str(tokens)
        }

        return response 