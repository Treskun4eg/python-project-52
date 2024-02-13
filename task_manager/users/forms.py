from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, SetPasswordForm, UserCreationForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext_lazy as _


class UserForm(UserCreationForm):

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "password1"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=True,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "password2"}),
        required=True,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super(UserUpdateForm, self).__init__(*args, **kwargs)
    #     del self.fields['password']

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2
