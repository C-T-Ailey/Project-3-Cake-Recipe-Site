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


# Create your views here.
def home(request):
    return render(request, 'home.html')



# Authentication Views

# Signup View - using new custom form in forms.py called NewUserForm to allow for email input on signup
def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid sign up - try again!"
    
    form = NewUserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# Password Change - specifying success url redirect, otherwise will default to a URL with the name 'password_change_done' which will need a new view & template specified.
class PasswordChange(PasswordChangeView):
  success_url = '/'
