from django_filters import FilterSet, filters
from .models import TasksModel
from task_manager.labels.models import LabelsModel
from django.utils.translation import gettext_lazy as _
from django import forms


class TaskFilter(FilterSet):

    label = filters.ModelChoiceFilter(queryset=LabelsModel.objects.all(),
                                      label=_('Label'),
                                      widget=forms.Select)

    self_tasks = filters.BooleanFilter(label=_('Self tasks'),
                                       method='get_self_tasks',
                                       lookup_expr='isnull',
                                       widget=forms.CheckboxInput)

    def get_self_tasks(self, queryset, name, value):
        lookup = queryset.filter(author=self.request.user)
        return lookup if value else queryset

    class Meta:
        model = TasksModel
        fields = ['status', 'executor', 'label', 'self_tasks']
