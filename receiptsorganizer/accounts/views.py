from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse

from django.views.generic import CreateView
# from django.contrib.auth.views import LoginView

from . import forms

class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


    


