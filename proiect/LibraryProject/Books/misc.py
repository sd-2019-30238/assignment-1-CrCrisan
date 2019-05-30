from django.shortcuts import render,redirect
from django.http import HttpResponse
from BookLoan.models import BookLoan
from Books.models import Book
from BookLoan.misc import *
from BookLoan.forms import AddLoan as BookLoanForms
from Books.forms import AddBook as BookForms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


class RequestAllBooks:
    def __init__(self, request, filter, ord):
        self.filter = filter
        self.request = request
        self.ord = ord
    def getFilter(self):
        return self.filter
    def getRequest(self):
        return self.request
    def getOrd(self):
        return self.ord

class RequestAllBooksHandle:
    BOOK_FILTERS = ['title', 'releaseDate', 'genre', 'author']
    def handle(self, requestObj):
        try:
            ordBy = requestObj.getFilter()
            ord = requestObj.getOrd()
            if ord == "descending":
                ordBy = "-"+ordBy
            books = Book.objects.all().order_by(ordBy)
        except:
            books = Book.objects.all()
        bestBook = Book.objects.all().order_by("-nrOfDownloads").first()
        return render(requestObj.getRequest(), 'Books/BooksList.html', {'books' : books, 'filters' : self.BOOK_FILTERS, 'bestBook' : bestBook})

class RequestSpecificBook:
    def __init__(self, request, slug):
        self.request = request
        self.slug = slug
    def getRequest(self):
        return self.request
    def getSlug(self):
        return self.slug

class RequestSpecificBookHandle:
    def handle(self, requestObj):
        book = Book.objects.get(slug=requestObj.getSlug())
        return render(requestObj.getRequest(), 'Books/BookDetail.html', {'book' : book})


class RequestAllLoans:
    def __init__(self, request, filter):
        self.request = request
        self.filter = filter
    def getRequest(self):
        return self.request
    def getFilter(self):
        return self.filter

class RequestAllLoansHandle:
    def handle(self, requestObj):
        loans = BookLoan.objects.all().order_by(requestObj.filter)
        return render(requestObj.getRequest(), 'BookLoan/AllLoans.html', {'loans' : loans})


class RequestSpecificLoan:
    def __init__(self, request, loanId):
        self.request = request
        self.loanId = loanId
    def getRequest(self):
        return self.request
    def getLoanId(self):
        return self.loanId

class RequestSpecificLoanHandle:
    def handle(self, requestObj):
        AproveCallBack(requestObj.loanId)
        loans = BookLoan.objects.get(id = requestObj.getLoanId())
        return render(requestObj.getRequest(), 'BookLoan/EditLoan.html', {'loan' : loans})


class RequestSpecificLoanE:
    def __init__(self, request, loanId):
        self.request = request
        self.loanId = loanId
    def getRequest(self):
        return self.request
    def getLoanId(self):
        return self.loanId

class RequestSpecificLoanHandleE:
    def handle(self, requestObj):
        loans = BookLoan.objects.get(id = requestObj.getLoanId())
        loanStatus = loans.status
        return render(requestObj.getRequest(), 'BookLoan/EditLoan.html', {'loan' : loans, 'loanStatus' : loanStatus})


class RequestUserLoans:
    def __init__(self, request, user, filter):
        self.request = request
        self.user = user
        self.filter = filter
    def getRequest(self):
        return self.request
    def getLoanUser(self):
        return self.user
    def getLoanFilter(self):
        return self.filter

class RequestUserLoansHandle:
    def handle(self, requestObj):
        loans = BookLoan.objects.filter(person = requestObj.getLoanUser()).order_by(requestObj.getLoanFilter())
        return render(requestObj.getRequest(), 'BookLoan/BookLoanList.html', {'loans':loans})


class AddLoan:
    def __init__(self, request, user, slug):
        self.request = request
        self.user = user
        self.slug = slug
    def getRequest(self):
        return self.request
    def getLoanUser(self):
        return self.user
    def getLoanSlug(self):
        return self.slug
class AddLoanHandle:
    def handle(self, requestObj):
        book = Book.objects.get(slug = requestObj.getLoanSlug())
        form = BookLoanForms()
        instance = form.save(commit = False)
        instance.person = requestObj.getLoanUser()
        instance.book = book
        instance.save()
        LoanCallBack(instance.id)
        return redirect("Book:list")

class RequestLoan:
    def __init__(self, request, slug):
        self.request = request
        self.slug = slug
    def getRequest(self):
        return self.request
    def getLoanSlug(self):
        return self.slug
class RequestLoanHandle:
    def handle(self, requestObj):
        book = Book.objects.get(slug = requestObj.getLoanSlug())
        return render(requestObj.getRequest(), 'BookLoan/BookLoan.html', {'book' : book})


class AddBookM:
    def __init__(self, request):
        self.request = request
    def getRequest(self):
        return self.request   

class AddBookHandle:
    def handle(self, requestObj):
        form = BookForms(requestObj.getRequest().POST, requestObj.getRequest().FILES)
        if form.is_valid():
            form.save()
            return redirect('Book:list')
        else:
            return render(requestObj.getRequest(), 'Books/AddBook.html', {'form':form})


class AddBookE:
    def __init__(self, request):
        self.request = request
    def getRequest(self):
        return self.request   

class AddBookEHandle:
    def handle(self, requestObj):
        form = BookForms()
        return render(requestObj.getRequest(), 'Books/AddBook.html', {'form':form})


class Singup:
    def __init__(self, request):
        self.request = request
    def getRequest(self):
        return self.request   

class SingupHandle:
    def handle(self, requestObj):
        form = UserCreationForm(requestObj.getRequest().POST)
        if form.is_valid():
            user = form.save()
            login(requestObj.getRequest(), user)
            return redirect("Book:list")
    

class Login:
    def __init__(self, request):
        self.request = request
    def getRequest(self):
        return self.request  

class LoginHandle:
    def handle(self, requestObj):
        form = AuthenticationForm(data = requestObj.getRequest().POST)
        if form.is_valid():
            user = form.get_user()
            login(requestObj.getRequest(), user)
            if 'next' in requestObj.getRequest().POST:
                return redirect(requestObj.getRequest().POST.get('next'))
            else:
                return redirect("Book:list")

handleDictio = {RequestAllBooks : RequestAllBooksHandle, RequestSpecificBook : RequestSpecificBookHandle,RequestAllLoans:RequestAllLoansHandle, RequestSpecificLoan:RequestSpecificLoanHandle,\
        RequestSpecificLoanE:RequestSpecificLoanHandleE, RequestUserLoans:RequestUserLoansHandle, AddLoan:AddLoanHandle,  RequestLoan:RequestLoanHandle, AddBookM:AddBookHandle, AddBookM:AddBookHandle,\
            AddBookE:AddBookEHandle, Singup:SingupHandle, Login:LoginHandle}

class Mediator:
    def mediate(self, reqObj):
    	return handleDictio[reqObj.__class__]().handle(reqObj)