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

        response = Response()
        response.delete_cookie('access_token')
        response.data = {
            "detail": "Account was succesfully logged out."
        }

        return response