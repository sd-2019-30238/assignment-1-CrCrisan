from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from Books.misc import *
# Create your views here.

mediator = Mediator()

def signupView(request):
    if request.method == 'POST':
        req = Singup(request)
        return mediator.mediate(req)
    else:
        form = UserCreationForm()
        return render(request, 'Accounts/Signup.html', {'form':form})

def loginView(request):
    if request.method == 'POST':
        req = Login(request)
        return mediator.mediate(req)
    else:
        form = AuthenticationForm()
    return render(request, 'Accounts/Login.html', {'form':form})

def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect("Book:list")