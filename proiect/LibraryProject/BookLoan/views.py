from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Books.models import Book
from . import forms
from .models import BookLoan

# Create your views here.

@login_required()
def newLoan(request, slug):
    book = Book.objects.get(slug = slug)

    if request.method == 'POST':
        form = forms.AddLoan()
        instance = form.save(commit = False)
        instance.person = request.user
        instance.book = book
        instance.save()
        return redirect("Book:list")
    else:
        return render(request, 'BookLoan/BookLoan.html', {'book' : book})


def myBookList(request):
    loans = BookLoan.objects.filter(person = request.user)
    
    return render(request, 'BookLoan/BookLoanList.html', {'loans':loans})