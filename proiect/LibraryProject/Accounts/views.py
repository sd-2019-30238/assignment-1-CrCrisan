from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signupView(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Book:list")
    else:
        form = UserCreationForm()
    return render(request, 'Accounts/Signup.html', {'form':form})