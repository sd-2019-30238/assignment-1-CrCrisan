from django.contrib import admin
from django.urls import path
from . import views

app_name = 'BookLoan'

urlpatterns = [
    path('all-loans/', views.AllLoans, name = 'allLoans'),
    path('loan-edit/<int:loanId>', views.EditLoan, name = 'editLoan'),
    path('my-list/', views.myBookList, name = "loanList"),
    path('return/<int:loanId>/', views.ReturnBook, name = 'returnBook'),
    path('<str:slug>/', views.newLoan, name = 'newLoan'),
]
