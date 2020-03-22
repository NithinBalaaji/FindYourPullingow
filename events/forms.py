from django import forms
from django.forms import ModelForm

from .models import Event


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'    



class EventCreationForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['event_name', 'content', 'date_event', 'time_event','group']
        widgets = {
            'date_event': DateInput(),
            'time_event': TimeInput

        }