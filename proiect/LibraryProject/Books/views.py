from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required, user_passes_test
from . import forms
from .misc import factory
from random import randint
BOOK_FILTERS = ['title', 'releaseDate', 'genre', 'author']

def bookList(request):
    if request.method == 'POST':
        try:
            ordBy = request.POST['OrdSelector']
            ord = request.POST.get('selectOrd', False) 
            if ord == "descending":
                ordBy = "-"+ordBy
            books = Book.objects.all().order_by(ordBy)
        except:
            books = Book.objects.all()
    else:
        books = Book.objects.all()
    i = randint(0, 1)
    if i == 0:
        rec = factory().getObj("nrOfDownloads")
    else:
        rec = factory().getObj("releaseDate")

    bestBook = rec.getBestBook()
    return render(request, 'Books/BooksList.html', {'books' : books, 'filters' : BOOK_FILTERS, 'bestBook' : bestBook})

def bookDetail(request, slug):
    book = Book.objects.get(slug = slug)
    return render(request, 'Books/BookDetail.html', {'book' : book})

def isEmployee(user):
    return user.groups.filter(name = 'Employees').exists()

@login_required()
@user_passes_test(isEmployee)
def addBook(request):
    if request.method == 'POST':
        form = forms.AddBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Book:list')
        else:
            return render(request, 'Books/AddBook.html', {'form':form})
    else:
        form = forms.AddBook()
    return render(request, 'Books/AddBook.html', {'form':form})