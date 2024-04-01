from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from crm.models import Member
from crm.serializers import MemberSerializer
from crm.permissions import IsTenantMember

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsTenantMember, ]

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Creating members is not allowed."}, status=status.HTTP_403_FORBIDDEN)
