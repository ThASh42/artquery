from django.test import TestCase
from querygenerator.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import get_user_model


class FormAuthenticationTestCase(TestCase):
    def setUp(self) -> None:
        self.client_username = 'clientuser'
        self.client_email = 'client@gmail.comm'
        self.client_password = 'clientpassword123'
        self.client_data = {
            'username': self.client_username,
            'email': self.client_email,
            'password': self.client_password,
        }
        self.client = get_user_model().objects.create_user(**self.client_data)
        return super().setUp()

    def test_user_registration_form_valid_data(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'test_password193',
            'password2': 'test_password193',
        })
        self.assertTrue(form.is_valid())
    
    def test_user_registration_form_invalid_data(self):
        '''
            Password can’t be too similar to your other personal information.
            Password must contain at least 8 characters.
            Password can’t be a commonly used password.
            Password can’t be entirely numeric.
            Two password fields must match.
        '''
        def assert_wrong_registration_data(data: dict) -> None:
            form = CustomUserCreationForm(data)
            self.assertFalse(form.is_valid())
        
        test_cases = [
            { # Similar to your other personal information
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': 'testuser01',
                    'password2': 'testuser01',
            },
            { # Does not contain at least 8 characters.
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': 'hello1a',
                    'password2': 'hello1a',
            },
            { # Commonly used password.
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': 'password',
                    'password2': 'password',
            },
            { # Entirely numeric
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': '19539582916',
                    'password2': '19539582916',
            },
            { # Two password fields didn’t match.
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': 'test_the_passwrd1052',
                    'password2': 'test_a_passwrd9999',
            },
        ]
        for case in test_cases:
            assert_wrong_registration_data(case)

    def test_user_registration_form_no_data(self):
        
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())

    def test_user_login_form_valid_data(self):
        form = CustomAuthenticationForm(data={
            'username': self.client_username,
            'password': self.client_password,
        })
        self.assertTrue(form.is_valid())
    
    def test_user_login_form_invalid_data(self):
        '''
            Values must be case-sensitive
        '''
        def assert_wrong_login_data(data: dict) -> None:
            form = CustomAuthenticationForm(data)
            self.assertFalse(form.is_valid())
        test_cases = [
            { # Check upper case sensitivity (uppercase)
                'username': self.client_username.upper(),
                'password': self.client_password.upper(),
            },
            { # Check upper case sensitivity (lowercase)
                'username': self.client_username.lower(),
                'password': self.client_password.lower(),
            },
        ]
        for case in test_cases:
            assert_wrong_login_data(case)

    def test_user_login_form_no_data(self):
        form = CustomAuthenticationForm(data={})
        self.assertFalse(form.is_valid())
