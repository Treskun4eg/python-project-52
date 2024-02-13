from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _


def index(request):
    return render(request, 'index.html')


class UserLoginFormView(LoginView):
    template_name = 'form.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('index')
    success_message = _('You are logged in')
    extra_context = {
        'title': _('Вход'),
        'button_text': _('Войти'),
    }


class UserLogoutFormView(LogoutView):
    next_page = reverse_lazy('index')
    success_message = _('You are logged out')
