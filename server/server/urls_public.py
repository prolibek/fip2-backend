from django.urls import path, include
from users.views import *

from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('organisations', OrganisationViewSet, basename='organisations')
    
urlpatterns = [
    path('api/v1/public/users/register/', RegisterAPIView.as_view(), name='register'),
    path('api/v1/public/users/login/', LoginAPIView.as_view(), name='login'),
    path('api/v1/public/users/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/v1/public/users/refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('api/v1/public/', include(router.urls)),
]