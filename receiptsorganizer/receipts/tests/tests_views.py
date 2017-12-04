from django.urls import resolve, reverse
from django.test import TestCase

from django.contrib.auth.models import User

from ..models import Category
from ..views import HomePageView, CategoriesView


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


class CategoriesViewTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='Yannick',
                email='r@gmail.com',password='testpassword1')
        Category.objects.create(name='Category Test',description='Description 1',
                created_by=self.user)
        self.client.login(username='Yannick',password='testpassword1')
        url = reverse('categories')
        self.response = self.client.get(url)

    def test_categories_view_status_code_if_logged(self):
        self.assertEquals(self.response.status_code,200)
    
    def test_categories_use_the_proper_template(self):
        self.assertTemplateUsed('categories.html')

    def test_categories_view_status_code_if_NOT_logged(self):
        self.client.logout()
        url = reverse('categories')
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 302)

    def test_category_url_resolve_to_category_listview(self):
        view = resolve('/categories/')
        self.assertEquals(view.func.view_class, CategoriesView)

    def test_categories_queryset(self):
        queryset = Category.objects.filter(created_by=self.user)
        self.assertIn('Category Test',str(queryset))
        self.assertContains(self.response,'Category Test')

    def test_category_page_contains_link_to_new_category(self):
        new_category_url = reverse('new_category')
        self.assertContains(self.response,'href="{0}"'.format(new_category_url))



