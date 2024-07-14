from crm.models import Resume, ResumeFile, Interview
from crm.serializers import ResumeListSerializer, ResumeDetailSerializer, InterviewSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()

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
    
    @action(detail=True, methods=['GET', 'POST'], permission_classes=[IsAuthenticated,])
    def interviews(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        
        if request.method == 'GET':
            interviews = Interview.objects.filter(resume=pk).values()
            return Response({"interviews": interviews})
        
        elif request.method == 'POST':
            serializer = InterviewSerializer(data={**request.data, "resume": pk})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)