from django.shortcuts import render, redirect
from django.views import View

from task_manager.registration.forms import UserRegistrationForm


# Create your views here.
class UserRegistrationFormView(View):

    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, 'registration/registration_form.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorization_user')
        return render(request, 'registration/registration_form.html', context={'form': form})
