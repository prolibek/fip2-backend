from rest_framework.permissions import BasePermission, SAFE_METHODS

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
        return super().has_permission(request, view) and (request.role == 1)

class IsHROrViewOnly(IsTenantMember):
    def has_permission(self, request, view):
        if super().has_permission(request, view) and request.method in SAFE_METHODS:
            return True
        return super().has_permission(request, view) and (request.user.role == 1)

class IsManagerAndTenantMember(IsTenantMember):
    def has_permission(self, request, view):
        return super().has_permission(self, request, view) and (request.role == 2)