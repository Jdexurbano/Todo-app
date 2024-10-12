from django.urls import path
from .views import CustomSignUpView,CustomLoginView,CustomLogoutView
urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),
    path('signup/',CustomSignUpView.as_view(),name='signup'),
]