from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from . import forms

def bookList(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'Books/BooksList.html', {'books' : books})

def bookDetail(request, slug):
    book = Book.objects.get(slug = slug)
    return render(request, 'Books/BookDetail.html', {'book' : book})

@login_required()
def addBook(request):
    if request.method == 'POST':
        form = forms.AddBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('Book:list')
    else:
        form = forms.AddBook()
    return render(request, 'Books/AddBook.html', {'form':form})