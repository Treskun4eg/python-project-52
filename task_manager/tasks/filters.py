from django_filters import FilterSet, filters
import django_filters
from .models import TasksModel
from task_manager.labels.models import LabelsModel
from django.utils.translation import gettext_lazy as _
from django import forms


class TaskFilter(FilterSet):

    labels = django_filters.ModelChoiceFilter(
        label=_('Label'),
        queryset=lambda req: LabelsModel.objects.all(),)

    self_tasks = filters.BooleanFilter(label=_('Self tasks'),
                                       method='get_self_tasks',
                                       lookup_expr='isnull',
                                       widget=forms.CheckboxInput)

    def get_self_tasks(self, queryset, name, value):
        lookup = queryset.filter(author=self.request.user)
        return lookup if value else queryset

    class Meta:
        model = TasksModel
        fields = ['status', 'executor', 'labels', 'self_tasks']
