from django.urls import path, include

from crm.views import *

from rest_framework.routers import DefaultRouter

from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()

router.register(r'organisations', OrganisationViewSet, basename='organisation')
router.register(r'vacancies', VacancyViewSet, basename='vacancy')

organisation_nested_router = NestedSimpleRouter(router, r'organisations', lookup='organisation')
organisation_nested_router.register(r'departments', DepartmentViewSet, basename='organisations-departments')
organisation_nested_router.register(r'vacancies', VacancyViewSet, basename='organisations-vacancies')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(organisation_nested_router.urls)),
]