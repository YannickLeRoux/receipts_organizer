from django.urls import resolve, reverse
from django.test import TestCase

from django.contrib.auth.models import User

from ..models import Category, Receipt
from ..views import ReceiptListView


class ReceiptListViewTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='Yannick',
                email='r@gmail.com',password='testpassword1')
        Category.objects.create(name='Category Test',description='Description 1',
                created_by=self.user)
        self.client.login(username='Yannick',password='testpassword1')
        url = reverse('receipts')
        self.response = self.client.get(url)

    def test_receipt_list_view_status_code_if_logged(self):
        self.assertEquals(self.response.status_code,200)
    
    def test_receipt_list_use_the_proper_template(self):
        self.assertTemplateUsed('receipts.html')

    def test_receipt_list_view_status_code_if_NOT_logged(self):
        self.client.logout()
        url = reverse('receipts')
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 302)

    def test_receipt_list_url_resolve_to_receiptlistview(self):
        view = resolve('/receipts/')
        self.assertEquals(view.func.view_class, ReceiptListView)

