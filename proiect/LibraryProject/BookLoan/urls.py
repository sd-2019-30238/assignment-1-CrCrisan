from django.contrib import admin
from django.urls import path
from . import views

app_name = 'BookLoan'

urlpatterns = [
    path('my-list/', views.myBookList, name = "loanList"),
    path('<str:slug>/', views.newLoan, name = 'newLoan'),
]
