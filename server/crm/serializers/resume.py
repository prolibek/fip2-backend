from rest_framework import serializers

from crm.models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    model = Resume
    fields = '__all__'