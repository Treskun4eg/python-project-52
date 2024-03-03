from .models import LabelsModel
from django import forms


class LabelsForm(forms.ModelForm):

    class Meta:
        model = LabelsModel
        fields = ['name']
