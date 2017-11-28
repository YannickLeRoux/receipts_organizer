from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import resolve, reverse
from django.test import TestCase

from ..views import SignUpView, LogInView

##### SIGNUP VIEW #####

class SignUpViewTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_page_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolve_to_SignUpView(self):
        view = resolve('/signup/')
        self.assertEquals(view.func.view_class, SignUpView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)


class SuccessfulSignUpTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        data = {
                'username':'john',
                'email': 'g1234@gmail.com',
                'password1':'testpassword',
                'password2':'testpassword',
                }
        self.response = self.client.post(url, data)
        self.login_url = reverse('login')

    def test_redirection(self):
        '''
        A valid signup should redirect to the login page

        '''
        self.assertRedirects(self.response, self.login_url)

    def test_user_creation(self):
        '''
        Check a user has been created in the db 
        '''

        self.assertTrue(User.objects.exists())

class InvalidSignUpTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  # submit an empty dictionary

    def test_signup_status_code(self):
        '''
        An invalid form submission should return to the same page
        '''
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())

##### LOGIN VIEW #####


class LogInViewTests(TestCase):

    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_login_page_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_login_url_resolve_to_LogInView(self):
        view = resolve('/login/')
        self.assertEquals(view.func.view_class, LogInView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, AuthenticationForm)


