from django_filters import FilterSet, filters
from .models import TasksModel
from task_manager.labels.models import LabelsModel
from django.utils.translation import gettext_lazy as _


class TaskFilter(FilterSet):

    labels = filters.ModelChoiceFilter(queryset=LabelsModel.objects.all(),
                                       label=_('Label'))

    class Meta:
        model = TasksModel
        fields = ['status', 'executor', 'labels']
