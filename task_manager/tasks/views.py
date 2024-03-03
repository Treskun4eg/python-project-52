from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import DeleteProtectionMixin
from django.urls import reverse_lazy

from .models import TasksModel
from .forms import TaskForm

from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.filters import TaskFilter
from django_filters.views import FilterView


class TasksIndexView(LoginRequiredMixin, FilterView):

    template_name = 'tasks/index.html'
    model = TasksModel
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show'),
    }


class TaskCreateFormView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    template_name = 'form.html'
    model = TasksModel
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task successfully created')
    extra_context = {
        'title': _('Create task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateFormView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    model = TasksModel
    form_class = TaskForm
    template_name = 'form.html'
    success_url = reverse_lazy('tasks_index')
    success_message = 'Task changed successfully'
    extra_context = {
        'title': _('Change of task'),
        'button_text': _('Update'),
    }


class TaskDeleteFormView(SuccessMessageMixin, LoginRequiredMixin,
                         DeleteProtectionMixin, DeleteView):

    model = TasksModel
    template_name = 'tasks/delete.html'
    protected_message = _('You cannot delete task while it is in use')
    protected_url = reverse_lazy('tasks_index')
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task deleted successfully')
    extra_context = {
        'title': _('Deleting a task'),
        'button_text': _('Delete'),
    }
