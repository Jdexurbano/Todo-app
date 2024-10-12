from django.urls import path
from .views import CustomSignUpView,CustomLoginView
urlpatterns = [
    path('',CustomLoginView.as_view(),name='login'),
]