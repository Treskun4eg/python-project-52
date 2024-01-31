from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from task_manager.users.forms import UserRegistrationForm, UserAuthorizationForm
from django.contrib import auth


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserRegistrationFormView(View):

    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, 'users/registration_form.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorization_user')
        return render(request, 'users/registration_form.html', context={'form': form})


class UserAuthorizationFormView(View):

    def get(self, request, *args, **kwargs):
        form = UserAuthorizationForm()
        return render(request, 'users/authorization_form.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = UserAuthorizationForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return redirect('users_index')

            return render(request, 'users/authorization_form.html', context={'form': form})

        return render(request, 'users/authorization_form.html', context={'form': form})
