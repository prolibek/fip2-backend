from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from crm.views import *

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()
router.register("departments", DepartmentViewSet, basename="departments")
router.register("vacancy-requests", VacancyRequestViewSet, basename="vacancy-requests")
router.register("vacancies", VacancyViewSet, basename="vacancies")
router.register("managers", ManagerViewSet, basename="managers")
router.register("members", MemberViewSet, basename="managers")

urlpatterns = [
    path('', include(router.urls)),
    path('invitation-create/', InvitationAPIView.as_view(), name='invitation'),
    path('invitation-accept/', InvitationAcceptAPIView.as_view(), name='invitation-accept'),
    path('vacancy-requests/', VacancyRequestStatusAPIView.as_view(), name='vacancy-requests'),
    path('vacancy-forms/', VacancyRequestFormCreate.as_view(), name='vacancy-forms'),
    path('vacancy-forms/<int:pk>/', VacancyRequestFormDetail.as_view(), name='vacancy-forms'),
    path('information/', OrganisationAPIView.as_view(), name='information')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)