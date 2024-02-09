from rest_framework.serializers import ModelSerializer

from crm.models import Resume

class ResumeListSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class ResumeDetailSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep["files"] = instance.resumefile_set.all().values()
        rep["comments"] = instance.resumecomment_set.all().values()

        return rep