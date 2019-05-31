from django import forms
from .models import User, Justificativa


class LoginForm(forms.ModelForm):
    Senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username']

class JustificativaForm(forms.ModelForm):
    justificativa = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Justificativa
        fields = ['justificativa']