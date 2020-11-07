from django import forms

from .models import Tender, Product, ProductCategory, Provider, Participant, Goods, Organization


class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ('name', 'description', 'creator', 'organization')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'measure', 'category')


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', )


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ('name', 'contact', 'phone_1', 'phone_2', 'email', 'description', 'inn', )


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('provider', 'tender', )


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('tender', 'product', )


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ('name', )
