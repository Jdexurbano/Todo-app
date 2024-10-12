from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'userauth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class CustomLogoutView(LogoutView):
    next_page = 'login'



class CustomSignUpView(CreateView):
    template_name = 'userauth/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')