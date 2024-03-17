from django.test import TestCase
from django.urls import reverse_lazy, reverse
from .models import LabelsModel
from task_manager.users.models import User


class LabelCreateFormViewTests(TestCase):

    fixtures = ['labels.json', 'users.json']

    def test_create_view(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('label_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(LabelsModel.objects.all().count(), 2)
        response = self.client.post(reverse_lazy('label_create'), {'name': 'new_label'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(LabelsModel.objects.all().count(), 3)

    def test_redirect_label(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(reverse_lazy('label_create'), {'name': 'new_status1'})
        self.assertRedirects(response, reverse_lazy('labels_index'))


class LabelUpdateFormViewTests(TestCase):

    fixtures = ['labels.json', 'users.json']

    def test_update_view(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(reverse('label_update', kwargs={'pk': 1}), {'name': 'update_label'})
        self.assertEqual(response.status_code, 302)
        status = LabelsModel.objects.get(pk=1)
        self.assertEqual(status.name, 'update_label')

    def test_update_redirect(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(reverse('label_update', kwargs={'pk': 1}), {'name': 'update_label'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_index'))


class LabelDeleteFormViewTests(TestCase):

    fixtures = ['labels.json', 'users.json']

    def test_delete_label(self):
        user = User.objects.get(pk=3)
        self.client.force_login(user=user)
        self.assertTrue(LabelsModel.objects.filter(pk=2).exists())
        response = self.client.post(reverse('label_delete', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(LabelsModel.objects.filter(pk=2).exists())
