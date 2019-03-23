from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Book'

urlpatterns = [
    path('', views.bookList, name = 'list'),
    path('add-book/', views.addBook, name = "add-book"),
    path('<str:slug>/', views.bookDetail, name = 'details'),
]
