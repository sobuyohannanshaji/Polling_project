from django.forms import ModelForm
from .models import *
from django import forms


class Register(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(),max_length=100)