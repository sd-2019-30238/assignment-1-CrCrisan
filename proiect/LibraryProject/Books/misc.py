from .models import Book

class BookQueryService:
    def getBook(self, tag):
        return Book.objects.get(slug = tag)
    
    def getBooks(self):
        return Book.objects.all()

    def getBooksOrd(self, ord):
        return Book.objects.all().order_by(ordBy)

class BookCommandService:
    def addBook(self, bookInstance):
        bookInstance.save()

class nrOfDownloads:
    def getBestBook(self):
        return Book.objects.all().order_by("-nrOfDownloads").first()

class byDate:
    def getBestBook(self):
        return Book.objects.all().order_by("-releaseDate").first()

class wrongName:
    def getBestBook(self):
        return None

class factory:
    def getObj(self, name):
        if name == "nrOfDownloads" :
            return nrOfDownloads()
        else:
            if name == "releaseDate":
                return byDate()
        return wrongName()