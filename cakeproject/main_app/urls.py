from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cakes/', views.cakes_index, name='index'),
    path('cakes/<int:cake_id>', views.cakes_detail, name='detail'),
    path('cakes/create', views.CakeCreate.as_view(), name='cakes_create'),
    path('cakes/<int:pk>/update', views.CakeUpdate.as_view(), name='cakes_update'),
    path('cakes/<int:pk>/delete', views.CakeDelete.as_view(), name='cakes_delete'),

    # Recipe
    #path('recipes/', views.RecipeList.as_view(), name='recipe_index'),
    #path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('cakes/<int:cake_id>/add_recipe', views.RecipeCreate.as_view(), name='add_recipe'),

    # Authentication Paths
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/password_change/', views.PasswordChange.as_view(), name='password_change'),
]