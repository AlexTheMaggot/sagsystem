# InternalImports
from . models import Customer
# End InternalImports

# DjangoImports
from django import forms
# End DjangoImports


# CustomerForm
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'date_of_birth', 'sex', 'address', 'telegram', 'facebook', 'instagram', 'comment')
# End CustomerForm
