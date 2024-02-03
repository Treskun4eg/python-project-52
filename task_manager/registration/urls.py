from django.urls import path
from task_manager.registration import views

urlpatterns = [
    path('', views.UserRegistrationFormView.as_view(), name='registration_user'),
]