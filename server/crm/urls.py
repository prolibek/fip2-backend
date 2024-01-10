from django.urls import path, include

from crm.views import *

from rest_framework.routers import DefaultRouter

from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()

router.register(r'organisations', OrganisationViewSet, basename='organisation')
router.register(r'vacancies', VacancyViewSet, basename='vacancy')

department_router = NestedSimpleRouter(router, r'organisations', lookup='organisation')
department_router.register(r'departments', DepartmentViewSet, basename='organisations-departments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(department_router.urls)),
]