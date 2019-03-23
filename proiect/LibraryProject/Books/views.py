from django.shortcuts import render
from django.http import HttpResponse
from . import models

def bookList(request):
    books = models.Book.objects.all().order_by('title')
    return render(request, 'Books/BooksList.html', {'books' : books})