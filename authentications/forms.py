from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import PasswordInput
from .models import Account

class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=16, min_length=8)
    password2 = forms.CharField(max_length=16, min_length=8)

    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_password2(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password2 != password1:
            raise ValidationError('passwords are not matching')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=16, min_length=8)