from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Category, Receipt


class ReceiptModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Yannick',
                email='r@gmail.com',password='testpassword1')
        self.category = Category.objects.create(name="CategoryName1",
                created_by=self.user)
        self.receipt = Receipt.objects.create(name="TestReceipt1",
                category=self.category, amount=100.00,recorded_by=self.user)

    def test_receipt_is_starts_with_REC(self):
        self.assertEquals(self.receipt.id[:3],"REC")

        


