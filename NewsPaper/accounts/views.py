from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm

from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

def logout(request):
    auth_logout(request)
    return redirect(request.META['HTTP_REFERER'])
