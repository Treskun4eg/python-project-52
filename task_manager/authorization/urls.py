from django.urls import path
from task_manager.authorization import views

urlpatterns = [
    path('', views.UserAuthorizationFormView.as_view(), name='authorization_user'),
    ]