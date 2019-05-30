from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from Books.models import Book
from . import forms
from .models import BookLoan
from .misc import ReturnCallBack, AproveCallBack, LoanCallBack
from Books.misc import *

mediator = Mediator()

@login_required()
def newLoan(request, slug):
    if request.method == 'POST':
        req = AddLoan(request, request.user, slug)
        return mediator.mediate(req)
    else:
        req = RequestLoan(request, slug)
        return mediator.mediate(req)

@login_required()
def myBookList(request):
    req = RequestUserLoans(request, request.user, '-date')
    return mediator.mediate(req)

def isEmployee(user):
    return user.groups.filter(name = 'Employees').exists()

@login_required()
@user_passes_test(isEmployee)
def EditLoan(request, loanId):
    if request.method == 'POST':
        req = RequestSpecificLoan(request, loanId)
        return mediator.mediate(req)
    else:
        req = RequestSpecificLoanE(request, loanId)
        return mediator.mediate(req)

@login_required()
@user_passes_test(isEmployee)
def AllLoans(request):
    req = RequestAllLoans(request, '-date')
    return mediator.mediate(req)

@login_required()
def ReturnBook(request, loanId):
    ReturnCallBack(loanId)
    return redirect("Book:list")
