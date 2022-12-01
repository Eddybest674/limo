from django.shortcuts import render
from django.contrib.auth.forms import*
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') #Why use reverse_lazy here instead of reverse? The reason is that for all generic class-based views the URLs are not loaded when the file is imported, so we have to use thelazy form of reverse to load them later when they’re available.
    template_name = 'accounts/signup.html'

# Create your views here.
