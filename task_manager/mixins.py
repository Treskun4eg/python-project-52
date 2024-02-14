from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from task_manager.users.models import User
from django.http import HttpResponseForbidden


class UserEditPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return self.request.user.has_perm('change_user') or self.request.user == user

    def handle_no_permission(self):
        return HttpResponseForbidden("У вас нет разрешения на редактирование этого пользователя.")
