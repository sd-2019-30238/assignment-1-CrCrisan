from django.contrib import admin
from django.urls import path
from . import views

app_name = 'BookLoan'

urlpatterns = [
    path('<str:slug>/', views.newLoan, name = 'newLoan'),
]
