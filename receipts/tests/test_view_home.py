from django.urls import resolve, reverse
from django.test import TestCase

from ..views import HomePageView


class HomePageViewTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_root_url_resolves_to_HomePageView(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)

    def test_home_page_returns_correct_html(self):
        self.assertEquals(self.response.status_code, 200)

        self.assertContains(self.response,'<html')
        self.assertContains(self.response,'Receipts Organizer')


