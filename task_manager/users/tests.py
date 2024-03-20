import json

from django.test import TestCase, Client
from django.urls import reverse_lazy, reverse
from task_manager.users.models import User

with open('task_manager/fixtures/user.json') as file:
    new_user = json.loads(file.read())

with open('task_manager/fixtures/user_invalid.json') as file:
    invalid_user = json.loads(file.read())


class UserRegistrationFormViewTests(TestCase):

    def test_create_view(self):
        response = self.client.post(
            reverse_lazy('registration_user'),
            new_user
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            User.objects.filter(username=new_user['username']).exists()
        )

    def test_redirect_user(self):
        response = self.client.post(
            reverse_lazy('registration_user'),
            new_user
        )
        self.assertRedirects(response, reverse_lazy('login_user'))

    def test_invalid_create_view(self):
        response = self.client.post(reverse('registration_user'), invalid_user)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            User.objects.filter(username=invalid_user['username']).exists()
        )


class UserUpdateFormViewTests(TestCase):

    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

    def test_update_view(self):
        test_user = dict(new_user)
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(
            reverse('update_user', args=[self.user1.id]),
            test_user
        )
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, test_user['username'])

    def test_update_logout(self):
        response = self.client.post(
            reverse('update_user', kwargs={'pk': 2})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users_index'))

    def test_invalid_update_view(self):
        update = {
            'username': 'new_value1 $%&*()',
            'password1': '12',
            'password2': '1',
        }
        user = User.objects.get(pk=2)
        self.client.force_login(user=user)
        response = self.client.post(
            reverse('update_user', kwargs={'pk': 2}),
            update
        )
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(pk=2)
        self.assertNotEqual(user.username, update['username'])


class UserDeleteFormViewTests(TestCase):

    fixtures = ['users.json']

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
