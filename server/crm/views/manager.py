from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from crm.serializers import ManagerSerializer
from crm.models import Manager, Member

from crm.permissions import IsTenantMember

class ManagerViewSet(ModelViewSet):
    permission_classes = (IsTenantMember,)
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()

    @action(detail=False, methods=['post'])
    def save_hierarchy(self, request):
        data = request.data.get('managers', []) 

        manager_ids = {}
        # Step 1: Create or update managers
        for manager_data in data:
            manager_id = manager_data.get('id')
            member_user_id = manager_data.get('member')
            if member_user_id:
                try:
                    member = Member.objects.get(user=member_user_id)
                except Member.DoesNotExist:
                    return Response({"error": "Member with user ID not found."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                member = None

            if manager_id:
                try:
                    manager = Manager.objects.get(id=manager_id)
                    # Update existing manager
                    manager_data['member'] = None if member is None else member.id
                    serializer = self.get_serializer(manager, data=manager_data, partial=True)
                except Manager.DoesNotExist:
                    # If manager does not exist, create a new one
                    manager_data['member'] = None if member is None else member.id
                    serializer = self.get_serializer(data=manager_data)
            else:
                # Create new manager
                manager_data['member'] = None if member is None else member.id
                serializer = self.get_serializer(data=manager_data)

            if serializer.is_valid():
                manager = serializer.save()
                manager_ids[manager.id] = manager  # Collect created/updated managers
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Step 2: Handle connections between managers
        for manager_data in data:
            manager_id = manager_data.get('id')
            parent_id = manager_data.get('parent_manager')  # Assuming you have a 'parent' field to connect managers

            if manager_id and parent_id:
                try:
                    manager = manager_ids.get(manager_id, Manager.objects.get(id=manager_id))
                    parent_manager = manager_ids.get(parent_id, Manager.objects.get(id=parent_id))
                    manager.parent = parent_manager
                    manager.save()
                except Manager.DoesNotExist:
                    return Response({"error": f"Manager with ID {manager_id} or {parent_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"status": "success"}, status=status.HTTP_200_OK)
