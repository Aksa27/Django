from django import forms 
from .models import *

class bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'