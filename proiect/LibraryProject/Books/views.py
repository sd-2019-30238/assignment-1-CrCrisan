from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required, user_passes_test
from . import forms
from Books.misc import *

mediator = Mediator()

BOOK_FILTERS = ['title', 'releaseDate', 'genre', 'author']

def bookList(request):
    if request.method == 'POST':
        try:
            req = RequestAllBooks(reques, request.POST['OrdSelector'], request.POST.get('selectOrd', False))
            return mediator.mediate(req)
        except:
            req = RequestAllBooks(request, None, None)
            return mediator.mediate(req)
    else:
        req = RequestAllBooks(request, None, None)
        return mediator.mediate(req)

def bookDetail(request, slug):
    req = RequestSpecificBook(request, slug)
    return mediator.mediate(req)
    
def isEmployee(user):
    return user.groups.filter(name = 'Employees').exists()

@login_required()
@user_passes_test(isEmployee)
def addBook(request):
    if request.method == 'POST':
        req = AddBookM(request)
        return mediator.mediate(req)
    else:
        req = AddBookE(request)
        return mediator.mediate(req)