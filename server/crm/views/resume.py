from rest_framework import views, viewsets

from crm.serializers import ResumeSerializer

class ResumeViewset(viewsets.ModelViewSet):
    serializer_class = Resume