from django import forms
from django.forms import ModelForm

from .models import Group



class GroupCreationForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'description', 'members']
        