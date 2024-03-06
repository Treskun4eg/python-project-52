from django.contrib import admin
from task_manager.users.models import User
from task_manager.statuses.models import StatusesModel
from task_manager.labels.models import LabelsModel
from task_manager.tasks.models import TasksModel

# Register your models here.
admin.site.register(User)
admin.site.register(StatusesModel)
admin.site.register(LabelsModel)
admin.site.register(TasksModel)
