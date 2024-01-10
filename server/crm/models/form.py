from django.db import models 

class Form(models.Model):
    VACANCY = 1
    CHARACTERISTICS = 2

    form_type = (
        (VACANCY, 'Vacancy'),
        (CHARACTERISTICS, 'Characteristics')
    )

class FormField(models.Model):
    SHORT_TEXT = 1
    LONG_TEXT = 2
    SELECT = 3 
    MULTISELECT = 4
    DATE = 5

    form_field_choices = (
        (SHORT_TEXT, 'Short'),
        (LONG_TEXT, 'Long'),
        (SELECT, 'Select'),
        (MULTISELECT, 'Multiselect'),
        (DATE, 'Date')
    )

    field_type = models.SmallIntegerField(choices=form_field_choices)
    field_name = models.CharField(max_length=55)

    form = models.ForeignKey(Form, on_delete=models.CASCADE)

class FormChoiceOptions(models.Model):
    option = models.CharField(max_length=55)