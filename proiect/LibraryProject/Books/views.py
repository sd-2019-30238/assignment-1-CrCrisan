from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bookList(request):
    return render(request, 'Books/BooksList.html')