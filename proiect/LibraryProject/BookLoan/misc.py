from Books.models import Book
from BookLoan.models import BookLoan
from .models import BookLoan

class LoanQueryService:
    def getLoanByPersonOrder(self, p, order):
        return BookLoan.objects.filter(person = p).order_by(order)

    def getLoan(self, lId):
        return BookLoan.objects.get(id = lId)
    
    def getLoans(self, order):
        return BookLoan.objects.all().order_by(order)

class LoanCommandService:
    def addLoan(self, loanInstance):
        loanInstance.save()

class Observer:
    def __init__(self):
        self.ObsList = []

    def attach(self, observer):
        if not observer in self.ObsList:
            self.ObsList.append(observer)

    def detach(self, observer):
        try:
            self.ObsList.ObsList.remove(observer)  
        except:
            pass      

    def Notify(self, arg):
        for observer in self.ObsList:
            if observer.book == arg:
                observer.Update(arg)

def CheckDeal(cupon):
    #toDo
    pass

def ReturnCallBack(loanId):
    loan = BookLoan.objects.get(id = loanId)
    book = loan.book
    loan.status = 'C'
    loan.save()
    pendingLoan = BookLoan.objects.filter(book = book, status = 'A').order_by("date")
    if len(pendingLoan) == 0:
        book = Book.objects.get(id = book.id)
        book.inSotck = True
        book.save()
    else:
        pendingLoan = pendingLoan[0]
        pendingLoan.status = 'O'
        pendingLoan.save()

def AproveCallBack(loanId):
    loan = BookLoan.objects.get(id = loanId)
    loan.status = 'A'
    book = loan.book
    if book.inStock == True :
        book.inStock = False
        book.save()
        loan.status = 'O'
    loan.save()

def LoanCallBack(loanId):
    loan = BookLoan.objects.get(id = loanId)
    book = loan.book
    book.nrOfDownloads += 1
    book.save()