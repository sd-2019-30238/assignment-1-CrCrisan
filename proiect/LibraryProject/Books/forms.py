from django import forms
from . import models

class AddBook(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'slug', 'description', 'releaseDate', 'author', 'genre', 'image', 'inStock']