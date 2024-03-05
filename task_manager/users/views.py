from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserEditPermissionMixin, DeleteProtectionMixin
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
        'title': _('Users')
    }


class UserRegistrationFormView(SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login_user')
    success_message = _('User successfully registered')
    extra_context = {
        'title': _('Registration'),
        'button_text': _('Register'),
    }


class UserUpdateFormView(SuccessMessageMixin, UserEditPermissionMixin, LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserForm
    template_name = 'form.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User successfully changed')
    extra_context = {
        'title': _('Edit'),
        'button_text': _('Update'),
    }


class UserDeleteFormView(SuccessMessageMixin, UserEditPermissionMixin,
                         LoginRequiredMixin, DeleteProtectionMixin, DeleteView):

    model = User
    template_name = 'users/delete_user.html'
    protected_message = _('Cannot delete user because it is in use')
    protected_url = reverse_lazy('users_index')
    success_url = reverse_lazy('users_index')
    success_message = _('User deleted successfully')
    extra_context = {
        'title': _('Deleting a user'),
        'button_text': _('Yes, delete'),
    }