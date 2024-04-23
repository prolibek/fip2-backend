from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.db.models import Q

from crm.permissions import IsTenantMember, IsHRAndTenantMember, IsHROrViewOnly
from crm.serializers import VacancySerializer, VacancyRequestSerializer, VacancyRequestStatusSerializer
from crm.models import VacancyRequest, Member, Manager, VacancyRequestStatus, Vacancy

def create_status_entities(manager, vacancyrequest, request):
    while manager.parent_manager is not None and manager.user != request.tenant.ceo:
        approval = VacancyRequestStatus.objects.create(
            request=vacancyrequest,
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
                manager=manager, 
                vacancyrequest=serializer.instance,
                request=request
            )
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        request_status_list = instance.vacancyrequeststatus_set.all().values()
        return Response(
            {
                **serializer.data,
                "status": request_status_list
            }
        )
    
    def destroy(self, request, *args, **kwargs):
        member = get_object_or_404(Member, user=request.user)

        instance = self.get_object()
        if instance.owner != member:
            return Response({
                "detail": "Only vacancy request owner can retract vacancy."
            }, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def my(self, request, *args, **kwargs):
        member = get_object_or_404(Member, user=request.user)
        user_requests = VacancyRequest.objects.filter(owner=member)
        
        serializer = VacancyRequestSerializer(user_requests, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def for_approval(self, request):
        member = get_object_or_404(Member, user=request.user)
    
        if request.user == request.tenant.ceo:
            return Response(
                VacancyRequestSerializer(
                    VacancyRequest.objects.exclude(owner=member).filter(ceo_approved=1), 
                    many=True
                ).data
            )
    
        manager = get_object_or_404(Manager, member=member)

        try:
            manager = Manager.objects.get(member=member)
        except Manager.DoesNotExist:
            return Response([])

        vacancy_requests = VacancyRequest.objects.filter(vacancyrequeststatus__approver=manager).distinct()
        
        serializer = VacancyRequestSerializer(vacancy_requests, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def approve(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.owner == request.tenant.ceo:
            return Response({
                "detail": "CEO cannot approve their own request."
            }, status=status.HTTP_400_BAD_REQUEST)

        if request.tenant.ceo == request.user and instance.owner != request.tenant.ceo:
            serializer = VacancyRequestSerializer(
                instance,
                data={ "ceo_approved": request.data['status'] },
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(
                    serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                )

        member = get_object_or_404(Member, user=request.user)
        manager = get_object_or_404(Manager, member=member)

        try:
            vstatus = VacancyRequestStatus.objects.get(
                request=instance, 
                approver=manager
            )
        except VacancyRequestStatus.DoesNotExist:
            return Response({
                "detail": "You are not eligible to set status for this vacancy."
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = VacancyRequestStatusSerializer(
            vstatus,
            data={
                "status": request.data["status"]
            },
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def fully_approved(self, request, *args, **kwargs):
        approved_requests = VacancyRequest.objects.filter(
            Q(ceo_approved=2) & (
                Q(vacancyrequeststatus__isnull=True) |
                Q(vacancyrequeststatus__status=2)
            )
        ).exclude(
            vacancy__isnull=False
        ).distinct()

        serializer = self.get_serializer(approved_requests, many=True)
        return Response(serializer.data)

class VacancyRequestStatusAPIView(APIView):
    def get_object(self, pk):
        try:
            return VacancyRequestStatus.objects.get(id=pk)
        except VacancyRequestStatus.DoesNotExist:
            return Response({
                "detail": "Object not found." 
            }, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        member = get_object_or_404(Member, user=request.user)
        manager = get_object_or_404(Manager, member=member)

        request_status = self.get_object(pk)

        if request_status.approver != manager:
            return Response({
                "detail": "You are not eligible to change this status."
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = VacancyRequestStatusSerializer(
            request_status,
            data={
                "status": request.data["status"]
            }, 
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

class VacancyViewSet(ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    permission_classes = (IsHROrViewOnly, )

    def create(self, request, *args, **kwargs):
        try:
            request_id = request.data['request']
        except:
            return Response({
                "detail": "Provide vacancy request before creating vacancy."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            vrequest = VacancyRequest.objects.get(id=request_id)
        except VacancyRequest.DoesNotExist:
            return Response({
                "detail": "Vacancy request not found."
            }, status=status.HTTP_404_NOT_FOUND)
        
        if Vacancy.objects.filter(vacancy_request=vrequest).exists():
            return Response({
                "detail": "A vacancy has already been created for this request."
            }, status=status.HTTP_403_FORBIDDEN)
        
        vstatuses = VacancyRequestStatus.objects.filter(id=request_id)
        
        if vstatuses:
            for vstatus in vstatuses:
                if vstatus.status != 2:
                    return Response({
                        "detail": "All superior managers and CEO must approve this request before creating vacancy."
                    }, status=status.HTTP_403_FORBIDDEN)
            
        serializer = VacancySerializer(
            data={
                "job_title": vrequest.job_title,
                "owner": vrequest.owner.id,
                "public_data": vrequest.public_data,
                "private_data": vrequest.private_data,
                "request": vrequest,
                "comments": request.data.get('comments'),
                "vacancy_request": request_id
            }
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    @action(detail=False, methods=['POST'])
    def manual(self, request, *args, **kwargs):
        serializer = VacancySerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    @action(detail=True, methods=['GET'])
    def resume(self, request, *args, **kwargs):
        pass