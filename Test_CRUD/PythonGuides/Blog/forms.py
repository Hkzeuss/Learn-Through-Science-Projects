from django import forms
from django.forms import ModelForm
from .models import Blog

class BlogForm(forms.ModelForm):  
    class Meta:  
        model = Blog
        fields = "__all__"

