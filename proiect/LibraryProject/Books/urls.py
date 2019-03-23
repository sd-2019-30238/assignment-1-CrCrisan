from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Book'

urlpatterns = [
    path('', views.bookList, name = 'list'),
    path('<str:slug>', views.bookDetail, name = 'details'),
]
