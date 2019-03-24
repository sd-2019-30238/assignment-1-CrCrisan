from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from . import forms

BOOK_FILTERS = ['title', 'releaseDate', 'genre', 'author']

def bookList(request):
    if request.method == 'POST':
        ordBy = request.POST['OrdSelector']
        ord = request.POST.get('selectOrd', False) 
        if ord == "descending":
            ordBy = "-"+ordBy
        books = Book.objects.all().order_by(ordBy)
    else:
        books = Book.objects.all()
    return render(request, 'Books/BooksList.html', {'books' : books, 'filters' : BOOK_FILTERS})

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
