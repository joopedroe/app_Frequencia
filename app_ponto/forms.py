from django import forms
from .models import User


class LoginForm(forms.ModelForm):
    Senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username']