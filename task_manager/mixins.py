from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
# from task_manager.users.models import User
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


class UserEditPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return self.request.user.has_perm('change_user') or self.request.user == user

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения другого пользователя.')
        return redirect(reverse_lazy('users_index'))
