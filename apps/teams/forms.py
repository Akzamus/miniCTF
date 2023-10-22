from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50, label="Team Name"
    )
    password = forms.CharField(
        max_length=250,
        min_length=8,
        label="Password",
        widget=forms.TextInput(attrs={'type': 'password'})
    )
