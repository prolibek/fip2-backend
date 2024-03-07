from crm.models import Resume 
from crm.serializers import ResumeListSerializer, ResumeDetailSerializer

from rest_framework.viewsets import ModelViewSet

class ResumeModelViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ResumeDetailSerializer
        return ResumeListSerializer