from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from crm.models import VacancyRequestForm, VacancyRequestFormField, FieldChoiceOptions

class VacancyRequestFormCreate(APIView):
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
