from django.contrib.auth import authenticate
from django.conf import settings
from django.middleware import csrf

from rest_framework import views, status
from rest_framework.response import Response

from users.models import Account

from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPIView(views.APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return Response({
                'detail': 'User not found.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({
                'detail': 'Password is incorrect.'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        response = Response()
        tokens = RefreshToken.for_user(user)

        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE'],
            expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            value = tokens.access_token,
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['HTTP_ONLY_SAMESITE']
        )

        csrf.get_token(request)

        response.data = tokens

        return response 