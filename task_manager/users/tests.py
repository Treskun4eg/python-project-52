import json

from django.test import TestCase
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

with open('task_manager/fixtures/user.json') as file:
    new_user = json.loads(file.read())

with open('task_manager/fixtures/user_invalid.json') as file:
    invalid_user = json.loads(file.read())


class UserRegistrationFormViewTests(TestCase):
    def test_create_view(self):
        response = self.client.post(reverse_lazy('registration_user'), new_user)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username=new_user['username']).exists())

    def test_redirect_user(self):
        response = self.client.post(reverse_lazy('registration_user'), new_user)
        self.assertRedirects(response, reverse_lazy('login_user'))

    def test_invalid_create_view(self):
        response = self.client.post(reverse('registration_user'), invalid_user)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username=invalid_user['username']).exists())


class UserUpdateFormViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(pk='2', username='test_user', password='qwe1234567')
        self.user.save()

    def test_update_view(self):
        update = {
            'username': 'new_value1',
            'password1': '12345678910',
            'password2': '12345678910'
        }
        user = User.objects.get(pk=2)
        self.client.force_login(user=user)
        response = self.client.post(reverse('update_user', kwargs={'pk': self.user.pk}), update)
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.username, update['username'])

    def test_update_logout(self):
        response = self.client.post(reverse('update_user', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users_index'))

    def test_invalid_update_view(self):
        update = {
            'username': 'new_value1\ $%&*()',
            'password1': '12',
            'password2': '1',
        }
        user = User.objects.get(pk=2)
        self.client.force_login(user=user)
        response = self.client.post(reverse('update_user', kwargs={'pk': self.user.pk}), update)
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        user = User.objects.get(pk=self.user.pk)
        self.assertNotEqual(user.username, update['username'])


class UserDeleteFormViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(pk='3', username='test_user2', password='qwe1234567')
        self.user = User.objects.create_user(pk='2', username='test_user3', password='qwe12345678')
        self.user.save()

    def test_delete_user(self):
        user = User.objects.get(pk=3)
        self.client.force_login(user=user)
        self.assertTrue(User.objects.filter(pk=3).exists())
        response = self.client.post(reverse('delete_user', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(pk=3).exists())

    def test_delete_logout(self):
        response = self.client.post(reverse('delete_user', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users_index'))

    def test_invalid_delete_view(self):
        user = User.objects.get(pk=3)
        self.client.force_login(user=user)
        response = self.client.get(reverse_lazy(
            'delete_user',
            kwargs={'pk': 2}
        ))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(pk='3').exists())
