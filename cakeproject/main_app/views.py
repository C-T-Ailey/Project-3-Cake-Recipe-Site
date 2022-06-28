from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cake, Recipe
from .forms import NewUserForm, RecipeForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView, LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

# Cake CRUD operations

class CakeDetail(DetailView):
    model = Cake
    def get_context_data(self, **kwargs):
        context = super(CakeDetail, self).get_context_data(**kwargs)
        context['form'] = RecipeForm
        return context

class CakeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cake
    fields = ['name', 'flavours', 'description', 'imageurl']
    success_message = "Cake successfully created."
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CakeUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cake
    fields = ['name', 'flavours', 'description', 'imageurl']
    success_message = "Cake successfully updated."
    
class CakeDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cake
    success_message = "Cake successfully deleted."
    success_url = '/cakes/'


# Home/Landing page

def home(request):
    return render(request, 'home.html')

def cakes_index(request):
    cakes = Cake.objects.all()
    return render(request, 'cakes/index.html', {'cakes': cakes})

def cakes_detail(request, pk):
    cake = Cake.objects.get(id=pk)
    recipe_form = RecipeForm
    return render(request, "cakes/detail.html", {'cake': cake, 'recipe_form': recipe_form})

# class RecipeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = Recipe
#     fields = ['title', 'description', 'ingredients', 'instructions', 'imageurl']
#     success_message = "Recipe successfully created."
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         form.instance.cake = self.request.cake_id
#         return super().form_valid(form)

"""@login_required
def add_feeding(request, cat_id):
    # where req.body in express represented the posted form data, django uses request.POST
    form = FeedingForm(request.POST)
    print(form)
    if form.is_valid():
        # Collect the data, but do not commit it to the DB
        new_feeding = form.save(commit=False)
        # sets the cat_id value of cat_id passed from the form(?)
        new_feeding.cat_id = cat_id
        # save to db
        new_feeding.save()
        return redirect('detail', cat_id = cat_id)"""

def add_recipe(request, pk):
    form = RecipeForm(request.POST)
    print(form)
    if form.is_valid():
        new_recipe = form.save(commit = False)
        new_recipe.cake_id = pk
        form.instance.created_by = request.user
        new_recipe.save()
        return redirect('detail', pk = pk)

# Authentication Views

# Signup View - using new custom form in forms.py called NewUserForm to allow for email input on signup
def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You successfully signed up and are now logged in.')
            return redirect('/')
        else:
            messages.error(request, "Invalid sign up - try again.")
            # error_message = "Invalid sign up - try again!"
    
    form = NewUserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# Password Change - specifying success url redirect, otherwise will default to a URL with the name 'password_change_done' which will need a new view & template specified.
class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    success_message = "Password changed successfully."
    success_url = '/'

class LoginView(SuccessMessageMixin, LoginView):
    success_message = "You have successfully logged in."


