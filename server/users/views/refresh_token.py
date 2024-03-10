from rest_framework import views, status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import UserRegisterSerializer
from users.models import Account

from django.conf import settings

class RefreshTokenAPIView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        print(refresh_token)

        if refresh_token is None:
            return Response({
                'detail': 'Refresh token is not valid.'
            }, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken(refresh_token)
        user = Account.objects.get(id=token['user_id'])

        # TOKEN ROTATION

        token.set_jti()
        token.set_exp()
        token.set_iat()

        response = Response({
            'access_token': str(token.access_token),
            'user': UserRegisterSerializer(user).data
        })

        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
            expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            value = str(token),
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )

        return response