from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'userauth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class CustomSignUpView(CreateView):
    template_name = 'userauth/signup.html'
    form_class = UserCreationForm

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class
    #     print(form)
    #     return render(request,self.template_name,{'form':form})