from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from crm.serializers import ResumeSerializer
from crm.models import Resume 

class ResumeViewSet(ModelViewSet):
    serializer_class = ResumeSerializer

    def get_queryset(self):
        return Resume.objects.filter(vacancy=self.kwargs['vacancy_id'])
    
    def create(self, request, *args, **kwargs):
        serializer = ResumeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(vacancy_id=kwargs['vacancy_id'])
            return Response(serializer.data)
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )