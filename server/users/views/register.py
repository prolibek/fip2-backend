from rest_framework import views, status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import UserRegisterSerializer

class RegisterAPIView(views.APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'detail': 'Invalid credentials.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()

        token = RefreshToken.for_user(user)
        
        return Response({
            'detail': 'Registration succesfully accomplished.',
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        }, status=status.HTTP_200_OK)