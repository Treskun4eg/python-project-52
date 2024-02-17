from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserEditPermissionMixin
from django.urls import reverse_lazy


# from .models import User
from django.contrib.auth.models import User

from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from task_manager.users.forms import UserForm
from django.utils.translation import gettext_lazy as _


# Create your views here.
class IndexView(ListView):

    template_name = 'users/index.html'
    model = User
    context_object_name = 'users'
    extra_context = {
        'title': _('Пользователи')
    }


class UserRegistrationFormView(SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login_user')
    success_message = _('Пользователь успешно зарегистрирован')
    extra_context = {
        'title': _('Регистрация'),
        'button_text': _('Зарегистрировать'),
    }


class UserUpdateFormView(SuccessMessageMixin, UserEditPermissionMixin, LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserForm
    template_name = 'form.html'
    success_url = reverse_lazy('users_index')
    success_message = 'Пользователь успешно изменен'
    extra_context = {
        'title': _('Редактировать'),
        'button_text': _('Изменить'),
    }


class UserDeleteFormView(SuccessMessageMixin, UserEditPermissionMixin,
                         LoginRequiredMixin, DeleteView):

    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('users_index')
    success_message = _('Пользователь успешно удален')
    extra_context = {
        'title': _('Удаление пользователя'),
        'button_text': _('Удалить'),
    }