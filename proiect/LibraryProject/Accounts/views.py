from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Book:list")
    else:
        form = UserCreationForm()
    return render(request, 'Accounts/Signup.html', {'form':form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("Book:list")
    else:
        form = AuthenticationForm()
    return render(request, 'Accounts/Login.html', {'form':form})

def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect("Book:list")