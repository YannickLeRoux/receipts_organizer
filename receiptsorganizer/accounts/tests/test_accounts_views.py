from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.views import LoginView
from ..views import SignUpView
from ..forms import SignUpForm

## SIGNUP TESTS

class SignUpViewTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_SignUpView_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolve_to_SignUpView(self):
        view = resolve('/signup/')
        self.assertEquals(view.func.view_class, SignUpView)

    def test_signup_view_contains_link_to_login(self):
        login_url = reverse('login')
        self.assertContains(self.response, 'href="{0}"'.format(login_url))

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        '''
        The view must contain five inputs: csrf, username, email,
        password1, password2
        '''
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)

        

class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email':'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.login_url = reverse('login')
        self.home_url = reverse('home')

    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the login page
        '''
        self.assertRedirects(self.response, self.login_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    # def test_user_authentication(self): TODO: voir si reponse sur commentaire
    # a ce sujet, comprends pas pourquoi user.is_aauthemticated si juste un
    # sign up
    #     '''
    #     Create a new request to an arbitrary page.
    #     The resulting response should now have an `user` to its context,
    #     after a successful sign up.
    #     '''
    #     response = self.client.get(self.home_url)
    #     user = response.context.get('user')
    #     self.assertTrue(user.is_authenticated)


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

## LOGIN TESTS

class LoginViewTests(TestCase):

    def setUp(self):
        User.objects.create_user(username='Yan',email='r@hotmail.com',password='testpassword')
        url = reverse('login')
        self.client.login(username='Yan',password='testpassword')
        self.response = self.client.get(url)
    
    def test_LoginView_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_login_url_resolve_to_LoginView(self):
        view = resolve('/login/')
        self.assertEquals(view.func.view_class, LoginView)

    def test_login_view_contains_link_to_signup_page(self):
        signup_url = reverse('signup')
        self.assertContains(self.response, 'href="{0}"'.format(signup_url))

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

#     def test_contains_form(self):
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        '''
        The view must contain three inputs: csrf, username,
        password,
        '''
        self.assertContains(self.response, '<input', 3)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="password"', 1)

class SuccessfulLogInTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='Yan',email='r@hotmail.com',password='testpassword')
        url = reverse('login')
        data = {'username':'Yan','password':'testpassword'}
        self.response = self.client.post(url,data)
    
    
    def test_redirection(self):
        '''
        A valid login form submission should redirect the user 
        to the todolists page
        '''
        self.lists_url = reverse('lists')
        self.assertRedirects(self.response, self.lists_url)


