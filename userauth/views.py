from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class CustomSignUpView(CreateView):
    template_name = 'userauth/signup.html'
    form_class = UserCreationForm

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class
    #     print(form)
    #     return render(request,self.template_name,{'form':form})