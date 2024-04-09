from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_tenants.utils import schema_context

from users.serializers import OrganisationSerializer
from crm.permissions import IsTenantMember, IsHRAndTenantMember

class OrganisationAPIView(APIView):
    permission_classes = []

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsTenantMember, ]
        else: 
            permission_classes = [IsHRAndTenantMember, ]
        
        return [permission() for permission in permission_classes]

    def get(self, request):
        try:
            serializer = OrganisationSerializer(request.tenant)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    def put(self, request):
        try:
            organisation_instance = request.tenant
            serializer = OrganisationSerializer(
                organisation_instance, 
                data=request.data, 
                partial=True
            )
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)