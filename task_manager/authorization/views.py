from django.shortcuts import render, redirect
from django.views import View

from task_manager.authorization.forms import UserAuthorizationForm
from django.contrib import auth


# Create your views here.
class UserAuthorizationFormView(View):

    def get(self, request, *args, **kwargs):
        form = UserAuthorizationForm()
        return render(request, 'authorization/authorization_form.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = UserAuthorizationForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return redirect('/')

            return render(request, 'authorization/authorization_form.html', context={'form': form})

        return render(request, 'authorization/authorization_form.html', context={'form': form})
