from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Authentication Paths
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/password_change/', views.PasswordChange.as_view(), name='password_change'),
]