from django.db import models 


class VacancyRequestForm(models.Model):
    form_title = models.CharField(max_length=255)

class VacancyRequestFormBlock(models.Model):
    block_name = models.CharField(max_length=255)

    form = models.ForeignKey(VacancyRequestForm, on_delete=models.CASCADE)

class VacancyRequestFormField(models.Model):
    SHORT_TEXT = 1
    LONG_TEXT = 2
    SELECT = 3 
    MULTISELECT = 4
    DATE = 5
    NUMBER = 6
    LIST = 7

    form_field_choices = (
        (SHORT_TEXT, 'Short'),
        (LONG_TEXT, 'Long'),
        (SELECT, 'Select'),
        (MULTISELECT, 'Multiselect'),
        (DATE, 'Date'),
        (NUMBER, 'Number'),
        (LIST, 'List'),
    )

    field_type = models.SmallIntegerField(choices=form_field_choices)
    field_name = models.CharField(max_length=55)

    form = models.ForeignKey(VacancyRequestForm, on_delete=models.CASCADE)

    block = models.ForeignKey(
        VacancyRequestFormBlock, 
        on_delete=models.CASCADE,
        null=True
    )

class FieldChoiceOptions(models.Model):
    option = models.CharField(max_length=128, null=True)
    field = models.ForeignKey(
        VacancyRequestFormField, 
        on_delete=models.CASCADE
    )
