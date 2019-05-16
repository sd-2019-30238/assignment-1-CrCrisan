from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from Books.models import Book
from . import forms
from .models import BookLoan
from .misc import ReturnCallBack, AproveCallBack, LoanCallBack, Observer, LoanQueryService, LoanCommandService, CheckDeal

# Create your views here.
gObs = Observer()
gLoanQuery = LoanQueryService()
gLoanCommand = LoanCommandService()

@login_required()
def newLoan(request, slug):
    book = Book.objects.get(slug = slug)
    if request.method == 'POST':
        cupon = request.POST.get("Coupon", False)
        CheckDeal(cupon)
        form = forms.AddLoan()
        instance = form.save(commit = False)
        instance.person = request.user
        instance.book = book
        gLoanCommand.addLoan(instance)
        LoanCallBack(instance.id)
        gObs.attach(instance)
        return redirect("Book:list")
    else:
        return render(request, 'BookLoan/BookLoan.html', {'book' : book})

@login_required()
def myBookList(request):
    loans = gLoanQuery.getLoanByPersonOrder(request.user, '-date')
    return render(request, 'BookLoan/BookLoanList.html', {'loans':loans})

def isEmployee(user):
    return user.groups.filter(name = 'Employees').exists()

@login_required()
@user_passes_test(isEmployee)
def EditLoan(request, loanId):
    if request.method == 'POST':
        AproveCallBack(loanId)
        loans = gLoanQuery.getLoan(loanId)
        return render(request, 'BookLoan/EditLoan.html', {'loan' : loans})
    else:
        loans = gLoanQuery.getLoan(loanId)
        loanStatus = loans.status
        return render(request, 'BookLoan/EditLoan.html', {'loan' : loans, 'loanStatus' : loanStatus})

@login_required()
@user_passes_test(isEmployee)
def AllLoans(request):
    loans = gLoanQuery.getLoans('-date')
    return render(request, 'BookLoan/AllLoans.html', {'loans' : loans})

@login_required()
def ReturnBook(request, loanId):
    obj = gLoanQuery.getLoan(loanId)
    ReturnCallBack(loanId)
    gObs.Notify(obj.book)
    return redirect("Book:list")