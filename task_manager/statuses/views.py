from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserEditPermissionMixin, DeleteProtectionMixin
from django.urls import reverse_lazy


# from .models import User
from .models import StatusesModel

from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from task_manager.statuses.forms import StatuseForm
from django.utils.translation import gettext_lazy as _


# Create your views here.
class StatusesIndexView(ListView):

    template_name = 'statuses/index.html'
    model = StatusesModel
    context_object_name = 'statuses'
    extra_context = {
        'title': _('Statuses')
    }


class StatusCreateFormView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    template_name = 'form.html'
    model = StatusesModel
    form_class = StatuseForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status successfully created')
    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create'),
    }


class StatusUpdateFormView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    model = StatusesModel
    form_class = StatuseForm
    template_name = 'form.html'
    success_url = reverse_lazy('statuses_index')
    success_message = 'Status changed successfully'
    extra_context = {
        'title': _('Change of status'),
        'button_text': _('Update'),
    }


class StatusDeleteFormView(SuccessMessageMixin, LoginRequiredMixin,
                           DeleteProtectionMixin, DeleteView):

    model = StatusesModel
    template_name = 'statuses/delete.html'
    protected_message = _('You cannot delete staus while it is in use')
    protected_url = reverse_lazy('statuses_index')
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status deleted successfully')
    extra_context = {
        'title': _('Deleting a status'),
        'button_text': _('Delete'),
    }
