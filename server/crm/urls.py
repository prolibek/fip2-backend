from django.urls import path, include

from crm.views import *

from rest_framework.routers import DefaultRouter

from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()

router.register(r'organisations', OrganisationViewSet, basename='organisations')
router.register(r'organisation-categories', OrganisationCategoryViewSet, basename='organisation-categories')
router.register(r'vacancy-categories', VacancyCategoryViewSet, basename='vacancy-categories')

organisation_router = NestedSimpleRouter(router, r'organisations', lookup='organisation')
organisation_router.register(r'departments', DepartmentViewSet, basename='departments')
organisation_router.register(r'vacancies', VacancyViewSet, basename='vacancies')
organisation_router.register(r'managers', ManagerViewSet, basename='managers')
organisation_router.register(r'vacancy_requests', VacancyRequestViewSet, basename='vacancy-requests')
vacancy_router = NestedSimpleRouter(organisation_router, r'vacancies', lookup='vacancy')
vacancy_router.register(r'resumes', ResumeViewSet, basename='resumes')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(organisation_router.urls)),
    path(r'', include(vacancy_router.urls)),
]