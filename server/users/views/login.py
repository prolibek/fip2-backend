from django.contrib.auth import authenticate
from django.conf import settings

from users.serializers import UserRegisterSerializer

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
        token = RefreshToken.for_user(user)

        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
            expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            value = str(token),
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )

        response.data = {
            'access_token': str(token.access_token),
            'user': UserRegisterSerializer(user).data
        }

        return response 