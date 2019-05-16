from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required, user_passes_test
from . import forms
from .misc import factory, BookCommandService, BookQueryService
from random import randint
BOOK_FILTERS = ['title', 'releaseDate', 'genre', 'author']

gBookCommand = BookCommandService()
gBookQuery = BookQueryService()
def bookList(request):
    if request.method == 'POST':
        try:
            ordBy = request.POST['OrdSelector']
            ord = request.POST.get('selectOrd', False) 
            if ord == "descending":
                ordBy = "-"+ordBy
            books = gBookQuery.getBooksOrd(ordBy)
        except:
            books = gBookQuery.getBooks()
    else:
        books = gBookQuery.getBooks()
    i = randint(0, 1)
    if i == 0:
        rec = factory().getObj("nrOfDownloads")
    else:
        rec = factory().getObj("releaseDate")

    bestBook = rec.getBestBook()
    return render(request, 'Books/BooksList.html', {'books' : books, 'filters' : BOOK_FILTERS, 'bestBook' : bestBook})

def bookDetail(request, slug):
    book = gBookQuery.getBook(slug)
    return render(request, 'Books/BookDetail.html', {'book' : book})

def isEmployee(user):
    return user.groups.filter(name = 'Employees').exists()

@login_required()
@user_passes_test(isEmployee)
def addBook(request):
    if request.method == 'POST':
        form = forms.AddBook(request.POST, request.FILES)
        if form.is_valid():
            gBookCommand.addBook(form)
            return redirect('Book:list')
        else:
            return render(request, 'Books/AddBook.html', {'form':form})
    else:
        form = forms.AddBook()
    return render(request, 'Books/AddBook.html', {'form':form})