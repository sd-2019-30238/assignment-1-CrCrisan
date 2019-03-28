from Books.models import Book
from BookLoan.models import BookLoan

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

    