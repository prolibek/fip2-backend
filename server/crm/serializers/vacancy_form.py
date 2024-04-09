from rest_framework.serializers import ModelSerializer, SerializerMethodField
from crm.models import VacancyRequestForm, VacancyRequestFormField, FieldChoiceOptions

class FieldChoiceOptionsSerializer(ModelSerializer):
    class Meta:
        model = FieldChoiceOptions
        fields = ['id', 'option']

class VacancyRequestFormFieldSerializer(ModelSerializer):
    options = FieldChoiceOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = VacancyRequestFormField
        fields = ['id', 'field_type', 'field_name', 'public', 'options']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.field_type in [VacancyRequestFormField.SELECT, VacancyRequestFormField.MULTISELECT]:
            representation['options'] = FieldChoiceOptionsSerializer(instance.fieldchoiceoptions_set.all(), many=True).data
        else:
            representation.pop('options', None)
        return representation

class VacancyRequestFormSerializer(ModelSerializer):
    fields = VacancyRequestFormFieldSerializer(many=True, source='vacancyrequestformfield_set')

    class Meta:
        model = VacancyRequestForm
        fields = ['id', 'form_title', 'fields']
