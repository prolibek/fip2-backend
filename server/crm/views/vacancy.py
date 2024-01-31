from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from crm.permissions import IsTenantMember
from crm.serializers import VacancySerializer, VacancyRequestSerializer, VacancyRequestStatusSerializer
from crm.models import VacancyRequest, Member, Manager, VacancyRequestStatus

def create_status_entities(manager, request):
    while manager.parent_manager is not None:
        approval = VacancyRequestStatus.objects.create(
            request=request,
            approver=manager.parent_manager
        )
        approval.save()
        manager = manager.parent_manager

class VacancyRequestViewSet(ModelViewSet):
    serializer_class = VacancyRequestSerializer
    queryset = VacancyRequest.objects.all()
    permission_classes = (IsTenantMember, )

    def create(self, request):
        serializer = VacancyRequestSerializer(data=request.data)
        member = Member.objects.get(user=request.user)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save(owner=member)

        manager = Manager.objects.filter(member=member).first()
        if manager:
            create_status_entities(
                manager, 
                serializer.instance
            )
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['GET'])
    def request_status(self, request, vacancyrequest, pk=None):
        request_status_list = vacancyrequest.vacancyrequeststatus_set.all().values()
        return Response(
            {
                "request": VacancyRequestSerializer(vacancyrequest),
                "status": VacancyRequestStatus(request_status_list, many=True)
            }
        )

