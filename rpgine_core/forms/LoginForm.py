from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=16, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)