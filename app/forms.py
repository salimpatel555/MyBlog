from django import forms
from django.db import models
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'user': forms.TextInput (attrs={'class':'form-control'}),
            'title': forms.TextInput (attrs={'class':'form-control'}),
            'description': forms.Textarea (attrs={'class':'form-control'}),
            'creat_at': forms.DateTimeInput(attrs={'class':'form-control'})
        }