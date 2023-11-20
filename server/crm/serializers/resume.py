from rest_framework.serializers import ModelSerializer

from crm.models import Resume

class ResumeSerializer(ModelSerializer):
    model = Resume
    fields = '__all__'