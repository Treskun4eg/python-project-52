from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='users_index'),
    path('login/', views.UserAuthorizationFormView.as_view(), name='authorization_user'),
    path('create/', views.UserRegistrationFormView.as_view(), name='registration_user'),
]
