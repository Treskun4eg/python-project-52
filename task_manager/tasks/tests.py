from django.test import TestCase
from django.urls import reverse_lazy, reverse
from .models import TasksModel
from task_manager.statuses.models import StatusesModel
from task_manager.users.models import User


class TaskCreateFormViewTests(TestCase):

    fixtures = ['statuses.json', 'users.json', 'tasks.json']

    def test_create_view(self):
        user = User.objects.get(pk=1)
        status = StatusesModel.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TasksModel.objects.all().count(), 3)
        response = self.client.post(
            reverse_lazy('task_create'),
            {
                'name': 'new_task',
                'status': status.id,
                'author': user.id
            }
        )
        self.assertEqual(response.status_code, 302)
        task = TasksModel.objects.get(pk=4)
        self.assertEqual(TasksModel.objects.all().count(), 4)
        self.assertEqual(task.__str__(), task.name)

    def test_redirect_task(self):
        user = User.objects.get(pk=1)
        status = StatusesModel.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(
            reverse_lazy('task_create'),
            {
                'name': 'new_task',
                'status': status.id,
                'author': user.id
            }
        )
        self.assertRedirects(response, reverse_lazy('tasks_index'))


class TaskUpdateFormViewTests(TestCase):

    fixtures = ['statuses.json', 'users.json', 'tasks.json']

    def test_update_view(self):
        user = User.objects.get(pk=2)
        status = StatusesModel.objects.get(pk=2)
        self.client.force_login(user=user)
        response = self.client.post(reverse('task_update', kwargs={'pk': 1}),
                                    {'name': 'update_task',
                                     'status': status.id,
                                     'author': user.id})
        self.assertEqual(response.status_code, 302)
        task = TasksModel.objects.get(pk=1)
        self.assertEqual(task.name, 'update_task')

    def test_update_redirect(self):
        user = User.objects.get(pk=1)
        status = StatusesModel.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(
            reverse('task_update', kwargs={'pk': 3}),
            {
                'name': 'update_task',
                'status': status.id,
                'author': user.id
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks_index'))


class TaskDeleteFormViewTests(TestCase):

    fixtures = ['statuses.json', 'users.json', 'tasks.json']

    def test_delete_task(self):
        user = User.objects.get(pk=3)
        self.client.force_login(user=user)
        self.assertTrue(TasksModel.objects.filter(pk=3).exists())
        response = self.client.post(reverse('task_delete', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(TasksModel.objects.filter(pk=3).exists())


class TaskListFilter(TestCase):

    fixtures = ['statuses.json', 'users.json', 'tasks.json']

    def test_task_filter(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(
            reverse_lazy('tasks_index'),
            {'executor': 1}
        )
        self.assertEqual(response.context['tasks'].count(), 1)
