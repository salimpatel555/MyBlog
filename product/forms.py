from django import forms
from django.db import models
from django.forms import fields
from.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput (attrs={'class':'form-control'}),
            'weight': forms.TextInput (attrs={'class':'form-control'}),
            'price': forms.TextInput (attrs={'class':'form-control'})
        }