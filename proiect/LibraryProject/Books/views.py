from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def bookList(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'Books/BooksList.html', {'books' : books})

def bookDetail(request, slug):
    book = Book.objects.get(slug = slug)
    return render(request, 'Books/BookDetail.html', {'book' : book})