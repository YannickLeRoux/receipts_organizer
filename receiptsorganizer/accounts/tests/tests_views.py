from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve, reverse
from django.test import TestCase

from ..views import SignUpView


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
# Create your tests here.
