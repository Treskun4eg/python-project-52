from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserEditPermissionMixin, DeleteProtectionMixin
from django.urls import reverse_lazy


# from .models import User
from .models import LabelsModel

from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from task_manager.labels.forms import LabelsForm
from django.utils.translation import gettext_lazy as _


# Create your views here.
class LabelsIndexView(ListView):

    template_name = 'labels/index.html'
    model = LabelsModel
    context_object_name = 'labels'
    extra_context = {
        'title': _('Labels')
    }


class LabelCreateFormView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    template_name = 'form.html'
    model = LabelsModel
    form_class = LabelsForm
    success_url = reverse_lazy('labels_index')
    success_message = _('Label successfully created')
    extra_context = {
        'title': _('Create Label'),
        'button_text': _('Create'),
    }


class LabelUpdateFormView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    model = LabelsModel
    form_class = LabelsForm
    template_name = 'form.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label changed successfully')
    extra_context = {
        'title': _('Change of label'),
        'button_text': _('Update'),
    }


class LabelDeleteFormView(SuccessMessageMixin, LoginRequiredMixin,
                          DeleteProtectionMixin, DeleteView):

    model = LabelsModel
    template_name = 'labels/delete.html'
    protected_message = _('You cannot delete label while it is in use')
    protected_url = reverse_lazy('labels_index')
    success_url = reverse_lazy('labels_index')
    success_message = _('Label deleted successfully')
    extra_context = {
        'title': _('Deleting a label'),
        'button_text': _('Yes, delete'),
    }
