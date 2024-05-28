from crm.models import Resume, ResumeFile
from crm.serializers import ResumeListSerializer, ResumeDetailSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

class ResumeViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ResumeDetailSerializer
        return ResumeListSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = ResumeDetailSerializer(data=request.data)

        if serializer.is_valid():
            resume = serializer.save()
        
            files = request.FILES.getlist('files')
            for file in files:
                ResumeFile.objects.create(resume=resume, file=file)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)