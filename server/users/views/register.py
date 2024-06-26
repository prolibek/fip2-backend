from rest_framework import views, status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import UserRegisterSerializer

from django.conf import settings

class RegisterAPIView(views.APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = serializer.save()

        token = RefreshToken.for_user(user)

        response = Response({
            'detail': 'Registration succesfully accomplished.',
            'access_token': str(token.access_token),
            'user': UserRegisterSerializer(user).data
        }, status=status.HTTP_200_OK)

        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
            expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            value = str(token),
            secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        
        return response