from .models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import password_validation
# from django.core.exceptions import ValidationError
# from django import forms
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class UserForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=150, required=True, label=_("First name")
    )
    last_name = forms.CharField(
        max_length=150, required=True, label=_("Last name")
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
            raise forms.ValidationError('A user with the same name already exists.')
        except User.DoesNotExist:
            return username

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
