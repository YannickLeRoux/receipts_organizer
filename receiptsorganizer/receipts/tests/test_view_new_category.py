from django.urls import resolve, reverse
from django.test import TestCase

from django.contrib.auth.models import User

from ..models import Category
from ..views import NewCategory


class NewCategoryTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Yannick',
                email='r@gmail.com',password='testpassword1')
        self.client.login(username='Yannick',password='testpassword1')
        url = reverse('new_category')
        self.response = self.client.get(url)

    def test_new_categories_view_status_code_if_logged(self):
        self.assertEquals(self.response.status_code,200)

    def test_NewCategories_view_status_code_if_NOT_logged(self):
        self.client.logout()
        url = reverse('new_category')
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 302)

    def test_new_categories_use_the_proper_template(self):
        self.assertTemplateUsed('new_category.html')

    def test_new_category_url_resolve_to_new_category_view(self):
        view = resolve('/categories/new/')
        self.assertEquals(view.func.view_class, NewCategory)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_creating_new_category_creates_new_object_created_by_user(self):
        url = reverse('new_category')
        data = {
                "name":"testreceipt", 
                "amount":100.00,
                }
        self.client.post(url, data)
        self.assertEquals(Category.objects.count(), 1)

        category = Category.objects.first()
        self.assertEquals(self.user,category.created_by)


