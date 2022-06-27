from django.shortcuts import render, redirect
from .models import Cake
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# Cake CRUD operations
#class CakeCreate(LoginRequiredMixin, CreateView):
class CakeCreate(CreateView):
    model = Cake
    fields = ['name', 'flavours', 'description', 'imageurl']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#class CakeUpdate(LoginRequiredMixin, UpdateView):
class CakeUpdate(UpdateView):
    model = Cake
    fields = ['name', 'flavours', 'description', 'imageurl']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
#class CakeDelete(LoginRequiredMixin, DeleteView):
class CakeDelete(DeleteView):
    model = Cake
    success_url = '/cakes/'


# Home/Landing page
def home(request):
    return render(request, 'home.html')

def cakes_index(request):
    cakes = Cake.objects.all()
    return render(request, 'cakes/index.html', {'cakes': cakes})

def cakes_detail(request, cake_id):
    cake = Cake.objects.get(id=cake_id)
    return render(request, "cakes/details.html", {'cake': cake})