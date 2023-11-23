from django import forms
from .models import*

class empform(forms.ModelForm):
    class Meta:
        model=emp
        fields='__all__'