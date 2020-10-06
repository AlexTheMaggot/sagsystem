from django import forms

from .models import Tender, Product


class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ('name',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'measure')
