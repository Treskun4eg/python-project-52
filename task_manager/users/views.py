from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, SetPasswordForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.views.generic.edit import BaseUpdateView

from task_manager.users.forms import UserForm
from django.utils.translation import gettext_lazy as _


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', {
            'users': users,
        })


class UserRegistrationFormView(CreateView):

    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('authorization_user')
    success_message = _('User is successfully registered')
    extra_context = {
        'title': _('Регистрация'),
        'button_text': _('Зарегистрировать'),
    }


class UserUpdateFormView(UpdateView):

    model = User
    form_class = UserForm
    template_name = 'form.html'
    success_url = reverse_lazy('users_index')
    success_message = 'User information updated successfully'
    extra_context = {
        'title': _('Редактировать'),
        'button_text': _('Изменить'),
    }
