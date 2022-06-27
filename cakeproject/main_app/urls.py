from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cakes/', views.cakes_index, name='index'),
    path('cakes/<int:cake_id>', views.cakes_detail, name='detail'),
    path('cakes/create', views.CakeCreate.as_view(), name='cakes_create'),
    path('cakes/<int:pk>/update', views.CakeUpdate.as_view(), name='cakes_update'),
    path('cakes/<int:pk>/delete', views.CakeDelete.as_view(), name='cakes_delete'),

    #path('cakes/<int:pk>/add_recipe', views.add_recipe, name='add_recipe'),

    # Authentication Paths
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
]