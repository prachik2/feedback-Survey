from django import forms
from django.forms import CheckboxInput
from django.forms.widgets import TextInput, Select

from base_app.models import Survey1, Survey2


class Survey1Form(forms.ModelForm):
    class Meta:
        model= Survey1
        exclude = ['date_added', 'date_updated']
        widgets = {
            'Name': TextInput(
                attrs={'class': 'form-control col-md-4', 'placeholder': 'Student Name'}),
            'Semester': Select(
                attrs={'class': 'form-control col-md-4', 'placeholder': 'Semester'}),
            'vote': TextInput(
                attrs={'class': 'form-control col-md-4', 'placeholder': 'How you Rank(1-5)'}),
            'missed_class': TextInput(
                attrs={'class': 'form-control col-md-4', 'placeholder': 'Missed Classes'}),
        }

    def clean(self):
        """Method to clean the department name.
        :return: cleaned_data, used in the views to further perform any validation and later
        used by save method.
        """
        cleaned_data = super(Survey1Form, self).clean()
        return cleaned_data


class Survey2Form(forms.ModelForm):
    class Meta:
        model= Survey2
        exclude = ['date_added', 'date_updated']
        widgets = {
            'Name': TextInput(
                attrs={'class': 'form-control col-md-4', 'placeholder': 'Student Name'}),
            'Semester': Select(
                attrs={'class': 'form-control col-md-4', 'placeholder': 'Semester'}),
            'vote': TextInput(
                attrs={'class': 'form-control col-md-4', 'placeholder': 'How you Rank(1-5)'}),
            'expected_topic': TextInput(
                attrs={'class': 'form-control col-md-4', 'placeholder': 'Expected Topic to learn'}),
            'is_class_off_time':CheckboxInput(
                attrs={'class': 'form-control col-md-4', 'placeholder': 'Class Start/End on time or not'}),
        }

    def clean(self):
        """Method to clean the department name.

        :return: cleaned_data, used in the views to further perform any validation and later
        used by save method.
        """
        cleaned_data = super(Survey2Form, self).clean()
        return cleaned_data