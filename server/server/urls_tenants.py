from django.urls import path, include

from crm.views import *

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()
router.register("departments", DepartmentViewSet, basename="departments")

urlpatterns = [
    path('', include(router.urls)),
    path('invitations/', InvitationAPIView.as_view(), name='invitation'),
]