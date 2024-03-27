from django.urls import path, include

from crm.views import *

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()
router.register("departments", DepartmentViewSet, basename="departments")
router.register("vacancy-requests", VacancyRequestViewSet, basename="vacancy-requests")
router.register("vacancies", VacancyViewSet, basename="vacancies")
router.register("managers", ManagerViewSet, basename="managers")

urlpatterns = [
    path('', include(router.urls)),
    path('invitations/', InvitationAPIView.as_view(), name='invitation'),
    path('vacancy-requests/', VacancyRequestStatusAPIView.as_view(), name='vacancy-requests'),
    path('vacancy-forms/', VacancyRequestFormCreate.as_view(), name='vacancy-forms')
]