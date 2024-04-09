from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from crm.models import VacancyRequestForm, VacancyRequestFormField, FieldChoiceOptions
from crm.permissions import IsHRAndTenantMember, IsTenantMember
from crm.serializers import VacancyRequestFormSerializer

class VacancyRequestFormCreate(APIView):
    permission_classes = [IsHRAndTenantMember, ]

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsTenantMember, ]
        else: 
            permission_classes = [IsHRAndTenantMember, ]
        
        return [permission() for permission in permission_classes]

    def get(self, request, format=None):
        queryset = VacancyRequestForm.objects.all().values()
        return Response(
            queryset
        )
    
    def post(self, request, format=None):
        data = request.data
        form_name = data.get('name')
        fields = data.get('fields', [])

        if not form_name or not fields:
            return Response({"error": "Missing form name or fields."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the VacancyRequestForm
        vacancy_request_form = VacancyRequestForm.objects.create(form_title=form_name)

        for field in fields:
            field_name = field.get('field_name')
            field_type = field.get('type')
            options = field.get('options', None)

            field_type_mapping = {
                'Short': VacancyRequestFormField.SHORT_TEXT,
                'Long': VacancyRequestFormField.LONG_TEXT,
                'Select': VacancyRequestFormField.SELECT,
                'Multiselect': VacancyRequestFormField.MULTISELECT,
                'Date': VacancyRequestFormField.DATE,
                'Number': VacancyRequestFormField.NUMBER
            }
            field_type_id = field_type_mapping.get(field_type)

            if field_type_id is None:
                continue

            form_field = VacancyRequestFormField.objects.create(
                field_type=field_type_id,
                field_name=field_name,
                form=vacancy_request_form
            )

            if options and field_type in ['Select', 'Multiselect']:
                options_list = options.split(';')
                for option in options_list:
                    FieldChoiceOptions.objects.create(option=option, field=form_field)

        return Response({"success": "Form created successfully."}, status=status.HTTP_201_CREATED)


class VacancyRequestFormDetail(APIView):
    permission_classes = [ IsTenantMember ]

    def get_object(self, pk):
        return get_object_or_404(VacancyRequestForm, id=pk)

    def get(self, request, pk, format=None):
        form = self.get_object(pk)
        serializer = VacancyRequestFormSerializer(form)

        return Response(serializer.data)