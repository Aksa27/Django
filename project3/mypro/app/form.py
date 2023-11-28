from django import forms
from app.models import Book
class bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'