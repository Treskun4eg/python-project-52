from django.test import TestCase
from django.urls import reverse_lazy, reverse
from .models import StatusesModel
from task_manager.users.models import User


class StatusCreateFormViewTests(TestCase):

    fixtures = ['statuses.json', 'users.json']

    def test_create_view(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('status_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(StatusesModel.objects.all().count(), 3)
        response = self.client.post(
            reverse_lazy('status_create'),
            {'name': 'new_status'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(StatusesModel.objects.all().count(), 4)

    def test_redirect_status(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(
            reverse_lazy('status_create'),
            {'name': 'new_status1'}
        )
        self.assertRedirects(response, reverse_lazy('statuses_index'))


class StatusUpdateFormViewTests(TestCase):

    fixtures = ['statuses.json', 'users.json']

    def test_update_view(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(
            reverse('status_update', kwargs={'pk': 1}),
            {'name': 'update_status'}
        )
        self.assertEqual(response.status_code, 302)
        status = StatusesModel.objects.get(pk=1)
        self.assertEqual(status.name, 'update_status')

    def test_update_redirect(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(reverse(
            'status_update', kwargs={'pk': 1}),
            {'name': 'update_status'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses_index'))


class StatusDeleteFormViewTests(TestCase):

    fixtures = ['statuses.json', 'users.json']

    def test_delete_status(self):
        user = User.objects.get(pk=3)
        self.client.force_login(user=user)
        self.assertTrue(StatusesModel.objects.filter(pk=3).exists())
        response = self.client.post(reverse('status_delete', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(StatusesModel.objects.filter(pk=3).exists())
