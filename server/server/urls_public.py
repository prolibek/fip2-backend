from django.urls import path, include
from users.views import *

from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework.routers import DefaultRouter

from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register('organisations', OrganisationViewSet, basename='organisations')


urlpatterns = [
    path('api/v1/public/users/register/', RegisterAPIView.as_view(), name='register'),
    path('api/v1/public/users/login/', LoginAPIView.as_view(), name='login'),
    path('api/v1/public/users/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/v1/public/users/refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('api/v1/public/', include(router.urls)),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]