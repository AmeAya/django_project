from django import forms
from .models import Product

class ProductCreationForm(forms.ModelForm): # ModelForm - Form для работы с модельками
    class Meta: # Meta - Основа класса
        model = Product
        fields = ('name', 'description', 'price', 'image')
        widgets = {
            'name': forms.TextInput,
            'description': forms.TextInput,
            'price': forms.NumberInput,
            'image': forms.FileInput
        }
