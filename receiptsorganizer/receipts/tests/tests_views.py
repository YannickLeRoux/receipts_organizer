from django.urls import resolve, reverse
from django.test import TestCase, RequestFactory
from django.http import HttpRequest

from ..views import HomePageView, SignUpView


class HomePageViewTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_root_url_resolves_to_HomePageView(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)

    def test_home_page_returns_correct_html(self):
        self.assertEquals(self.response.status_code, 200)

        self.assertContains(self.response,'<html>')
        self.assertContains(self.response,'<title>Receipts Organizer</title>')
        

class SignUpViewTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_page_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolve_to_SignUpView(self):
        view = resolve('/signup/')
        self.assertEquals(view.func.view_class, SignUpView)
# Create your tests here.
