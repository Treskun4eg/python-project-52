from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserAuthorizationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']
