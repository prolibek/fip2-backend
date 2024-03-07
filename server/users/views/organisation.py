from django.db import transaction, connection

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from users.serializers import OrganisationSerializer
from users.models import Organisation, Domain

from crm.models import Member

class OrganisationViewSet(ModelViewSet):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = OrganisationSerializer(data=request.data)

            if not serializer.is_valid():
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            serializer.save(
                schema_name=request.data['slug'],
                creator=request.user
            )

            organisation = serializer.instance

            domain = Domain.objects.create(
                domain=organisation.slug,
                tenant=organisation
            )
            domain.save()

            # go into tenant database and set creator as a member
            connection.set_tenant(organisation)
            member = Member.objects.create(
                organisation=organisation,
                user=request.user
            )
            member.save()



            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)