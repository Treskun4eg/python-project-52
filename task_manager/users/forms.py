from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            ]


class UserAuthorizationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']
