from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserEditPermissionMixin
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


class StatusCreateFormView(SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = StatusesModel
    form_class = StatuseForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status successfully created')
    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create'),
    }
#
#
# class UserUpdateFormView(SuccessMessageMixin, UserEditPermissionMixin, LoginRequiredMixin, UpdateView):
#
#     model = User
#     form_class = UserForm
#     template_name = 'form.html'
#     success_url = reverse_lazy('users_index')
#     success_message = 'Пользователь успешно изменен'
#     extra_context = {
#         'title': _('Редактировать'),
#         'button_text': _('Изменить'),
#     }
#
#
# class UserDeleteFormView(SuccessMessageMixin, UserEditPermissionMixin,
#                          LoginRequiredMixin, DeleteView):
#
#     model = User
#     template_name = 'users/delete_user.html'
#     success_url = reverse_lazy('users_index')
#     success_message = _('Пользователь успешно удален')
#     extra_context = {
#         'title': _('Удаление пользователя'),
#         'button_text': _('Удалить'),
#     }