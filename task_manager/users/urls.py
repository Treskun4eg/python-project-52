from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='users_index'),
    path('create/', views.UserRegistrationFormView.as_view(), name='registration_user'),
    path('<int:pk>/update/', views.UserUpdateFormView.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.UserDeleteFormView.as_view(), name='delete_user'),
]