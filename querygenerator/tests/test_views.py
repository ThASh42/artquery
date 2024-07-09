from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class AnonymousUserTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        return super().setUp()

    def test_index_view_GET(self):
        url = reverse('querygenerator:index')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'querygenerator/index.html')

    def test_register_view_GET(self):
        url = reverse('querygenerator:register')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'querygenerator/register.html')

    def test_login_view_GET(self):
        url = reverse('querygenerator:login')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'querygenerator/login.html')
    
    def test_logout_view_GET(self):
        url = reverse('querygenerator:logout')
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)
    
    def test_register_view_POST_blank_data(self):
        url = reverse('querygenerator:register')
        response = self.client.post(url, {})
        self.assertEqual(200, response.status_code)
    
    def test_register_view_POST_invalid_data(self):
        url = reverse('querygenerator:register')
        response = self.client.post(url, {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertEqual(200, response.status_code)
    
    def test_register_view_POST_valid_data(self):
        url = reverse('querygenerator:register')
        response = self.client.post(url, {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'test_password193',
            'password2': 'test_password193',
        })
        self.assertEqual(302, response.status_code)

class AuthenticatedUserTestCase(AnonymousUserTestCase):
    def setUp(self) -> None:
        self.client_username = 'clientuser'
        self.client_email = 'client@gmail.com'
        self.client_password = 'clientpassword123'
        self.client_data = {
            'username': self.client_username,
            'email': self.client_email,
            'password': self.client_password,
        }
        self.user = get_user_model().objects.create_user(**self.client_data)
        self.client.login(**self.client_data)
