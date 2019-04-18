from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from Books.models import Book
from . import forms
from .models import BookLoan
from .misc import ReturnCallBack, AproveCallBack, LoanCallBack, Observer

# Create your views here.
gObs = Observer()


@login_required()
def newLoan(request, slug):
    book = Book.objects.get(slug = slug)
    if request.method == 'POST':
        form = forms.AddLoan()
        instance = form.save(commit = False)
        instance.person = request.user
        instance.book = book
        instance.save()
        LoanCallBack(instance.id)
        gObs.attach(instance)
        return redirect("Book:list")
    else:
        return render(request, 'BookLoan/BookLoan.html', {'book' : book})

@login_required()
def myBookList(request):
    loans = BookLoan.objects.filter(person = request.user).order_by('-date')
    return render(request, 'BookLoan/BookLoanList.html', {'loans':loans})

def isEmployee(user):
    return user.groups.filter(name = 'Employees').exists()

@login_required()
@user_passes_test(isEmployee)
def EditLoan(request, loanId):
    if request.method == 'POST':
        AproveCallBack(loanId)
        loans = BookLoan.objects.get(id = loanId)
        return render(request, 'BookLoan/EditLoan.html', {'loan' : loans})
    else:
        loans = BookLoan.objects.get(id = loanId)
        loanStatus = loans.status
        return render(request, 'BookLoan/EditLoan.html', {'loan' : loans, 'loanStatus' : loanStatus})

@login_required()
@user_passes_test(isEmployee)
def AllLoans(request):
    loans = BookLoan.objects.all().order_by('-date')
    return render(request, 'BookLoan/AllLoans.html', {'loans' : loans})

@login_required()
def ReturnBook(request, loanId):
    obj = BookLoan.objects.get(id = loanId)
    ReturnCallBack(loanId)
    gObs.Notify(obj.book)
    return redirect("Book:list")