from .models import StatusesModel
from django import forms


class StatuseForm(forms.ModelForm):

    class Meta:
        model = StatusesModel
        fields = ['name']
