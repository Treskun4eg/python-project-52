from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('Менеджер задач')}


class UserLoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('index')
    success_message = _('Вы вошли в систему')
    extra_context = {
        'title': _('Вход'),
        'button_text': _('Войти'),
    }


class UserLogoutFormView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('index')
    success_message = _('Вы вышли из системы')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('Вы вышли из системы'))
        return super().dispatch(request, *args, **kwargs)
