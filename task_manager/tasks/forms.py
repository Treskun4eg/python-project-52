from .models import TasksModel
from django import forms


class TaskForm(forms.ModelForm):

    class Meta:
        model = TasksModel
        fields = ['name', 'description', 'status', 'executor', 'label']
