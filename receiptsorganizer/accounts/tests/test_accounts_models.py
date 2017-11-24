from django.test import TestCase
from ..models import User


class UserModelTests(TestCase):
    
    def setUp(self):
        self.user=User.objects.create(username='John',password='dancehall',
                email='rasyann@hotmail.com')

    def test_print_user_displays_username(self):
        self.assertEquals(str(self.user),'John')
