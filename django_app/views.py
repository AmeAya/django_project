from django.shortcuts import render
from django.views.generic import \
    ListView, \
    DetailView, \
    CreateView, \
    UpdateView, \
    DeleteView
from .models import *
from .forms import ProductCreationForm
from django.urls import reverse_lazy # same reverse, but not async

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    form_class = ProductCreationForm
    model = Product
    template_name = 'product_new.html'
    # fields = '__all__' #  same all fields

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    fields = ['name', 'description', 'price', 'image']

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('home') # redirect url after deleting object
