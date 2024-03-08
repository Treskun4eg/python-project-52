from .models import LabelsModel
from django import forms
from django.utils.translation import gettext_lazy as _


class LabelsForm(forms.ModelForm):

    class Meta:
        model = LabelsModel
        fields = ['name']
        labels = {
            'name': _('Name')
        }