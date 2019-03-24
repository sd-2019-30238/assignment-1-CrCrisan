from django import forms
from . import models

class AddLoan(forms.ModelForm):
    class Meta:
        model = models.BookLoan
        fields = ['person', 'book']