from rest_framework.serializers import ModelSerializer

from users.models import Organisation
from .account import AccountSerializer

class OrganisationCreateSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name', 'slug']

class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrganisationSerializer, self).__init__(*args, **kwargs)

        self.fields['ceo'].required = False
        self.fields['creator'].required = False
        self.fields['schema_name'].required = False