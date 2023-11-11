from rest_framework import views, status
from rest_framework.response import Response

from users.serializers import LogoutSerializer

class LogoutAPIView(views.APIView):
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "detail": "Failed to log out."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()

        return Response({
            "detail": "Account was succesfully logged out."
        }, status=status.HTTP_200_OK)