from rest_framework.permissions import BasePermission

from crm.models import Member

class IsTenantMember(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        member = Member.objects.filter(
            organisation=request.tenant, 
            user=request.user
        )

        if member:
            return True 
        return False

class IsHRAndTenantMember(IsTenantMember):
    def has_permission(self, request, view):
        return super().has_permission(self, request, view) and (request.role == 1)

class IsManagerAndTenantMember(IsTenantMember):
    def has_permission(self, request, view):
        return super().has_permission(self, request, view) and (request.role == 2)