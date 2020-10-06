from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Measure


class AuthLoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class MeasureForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = ('name', )
