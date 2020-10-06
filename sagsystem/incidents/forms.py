from django import forms

from .models import Incidents


class IncidentsForm(forms.ModelForm):
    class Meta:
        model = Incidents
        fields = ('date', 'worker', 'department', 'comment', 'adder', 'file')
