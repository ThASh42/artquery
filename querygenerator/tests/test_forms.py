from django.test import TestCase
from querygenerator.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import get_user_model


class FormRegistrationTestCase(TestCase):
    def setUp(self) -> None:
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
        STRING_MULTIPLIER: int = 50
        assert isinstance(STRING_MULTIPLIER, int)
        LONG_USERNAME: str = 'testuser' * STRING_MULTIPLIER
        LONG_MAIL: str = ('testuser' * STRING_MULTIPLIER) + '@gmail.com'
        LONG_PASSWORD: str = 'test_password193' * STRING_MULTIPLIER
        '''
            Password can’t be too similar to your other personal information.
            Password must contain at least 8 characters.
            Password can’t be a commonly used password.
            Password can’t be entirely numeric.
            Two password fields must match.
            Username and email must not be long
        '''
        def assert_wrong_registration_data(case: dict) -> None:
            form = CustomUserCreationForm(data=case['data'])
            self.assertFalse(form.is_valid())

            for error_list in form.errors.values():
                for error in error_list:
                    self.assertIn(error, case['error_messages'])
                    case['error_messages'].remove(error)
            self.assertFalse(case['error_messages'])
        
        test_cases = [
            { # Similar to your other personal information
                'data': {
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': 'testuser01',
                    'password2': 'testuser01',
                },
                'error_messages': ['The password is too similar to the username.'],
            },
            { # Does not contain at least 8 characters.
                'data': {
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': 'hello1a',
                    'password2': 'hello1a',
                },
                'error_messages': ['This password is too short. It must contain at least 8 characters.'],
            },
            { # Commonly used password.
                'data': {
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': 'password',
                    'password2': 'password',
                },
                'error_messages': ['This password is too common.'],
            },
            { # Entirely numeric
                'data': {
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': '19539582916',
                    'password2': '19539582916',
                },
                'error_messages': ['This password is entirely numeric.'],
            },
            { # Two password fields didn’t match.
                'data': {
                    'username': 'testuser',
                    'email': 'testuser@gmail.com',
                    'password1': 'test_the_passwrd1052',
                    'password2': 'test_a_passwrd9999',
                },
                'error_messages': ['The two password fields didn’t match.'],
            },
            { # Values must not be long
                'data': {
                    'username': LONG_USERNAME,
                    'email': LONG_MAIL,
                    'password1': LONG_PASSWORD,
                    'password2': LONG_PASSWORD,
                },
                'error_messages': [
                    f'Ensure this value has at most 150 characters (it has {len(LONG_USERNAME)}).',
                    f'Ensure this value has at most 254 characters (it has {len(LONG_MAIL)}).',
                    'Enter a valid email address.',
                ],
            },
        ]
        for case in test_cases:
            assert_wrong_registration_data(case)

    def test_user_registration_form_no_data(self):
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())


class FormLoginTestCase(TestCase):
    def setUp(self) -> None:
        ''' Username and password must be titled to check case sensitivity in further tests '''
        self.client_username = 'clientuser'.title()
        self.client_email = 'client@gmail.com'
        self.client_password = 'clientpassword123'.title()
        self.client_data = {
            'username': self.client_username,
            'email': self.client_email,
            'password': self.client_password,
        }
        self.client = get_user_model().objects.create_user(**self.client_data)
        return super().setUp()

    def test_user_login_form_valid_data(self):
        form = CustomAuthenticationForm(data={
            'username': self.client_username,
            'password': self.client_password,
        })
        self.assertTrue(form.is_valid())

    def test_user_login_form_invalid_data(self):
        DEFAULT_LOGIN_ERROR_MESSAGE = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        STRING_MULTIPLIER: int = 100
        assert isinstance(STRING_MULTIPLIER, int)
        LONG_USERNAME: str = self.client_username * STRING_MULTIPLIER
        LONG_PASSWORD: str = self.client_password * STRING_MULTIPLIER
        '''
            Values must be case-sensitive
            Username must not be long
        '''
        def assert_wrong_login_data(case: dict) -> None:
            form = CustomAuthenticationForm(data=case['data'])
            self.assertFalse(form.is_valid())

            for error_list in form.errors.values():
                for error in error_list:
                    self.assertIn(error, case['error_messages'])
                    case['error_messages'].remove(error)
            self.assertFalse(case['error_messages'])

        test_cases = [
            { # Check upper case sensitivity (uppercase)
                'data': {
                    'username': self.client_username.upper(),
                    'password': self.client_password.upper(),
                },
                'error_messages': [DEFAULT_LOGIN_ERROR_MESSAGE],
            },
            { # Check upper case sensitivity (lowercase)
                'data': {
                    'username': self.client_username.lower(),
                    'password': self.client_password.lower(),
                },
                'error_messages': [DEFAULT_LOGIN_ERROR_MESSAGE],
            },
            { # Username must not be long
                'data': {
                    'username': LONG_USERNAME * 100,
                    'password': LONG_PASSWORD * 100,
                },
                'error_messages': [DEFAULT_LOGIN_ERROR_MESSAGE],
            },
        ]
        for case in test_cases:
            assert_wrong_login_data(case)

    def test_user_login_form_no_data(self):
        form = CustomAuthenticationForm(data={})
        self.assertFalse(form.is_valid())
