from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cake, Recipe
from .forms import NewUserForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

# Cake CRUD operations

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
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
    
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

def cakes_detail(request, cake_id):
    cake = Cake.objects.get(id=cake_id)
    return render(request, "cakes/detail.html", {'cake': cake})


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




