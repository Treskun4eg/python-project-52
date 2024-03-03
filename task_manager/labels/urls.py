from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelsIndexView.as_view(), name='labels_index'),
    path('create/', views.LabelCreateFormView.as_view(), name='label_create'),
    path('<int:pk>/update/', views.LabelUpdateFormView.as_view(), name='label_update'),
    path('<int:pk>/delete/', views.LabelDeleteFormView.as_view(), name='label_delete'),
]