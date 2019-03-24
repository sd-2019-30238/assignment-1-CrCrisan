from django.contrib import admin
from django.urls import path
from . import views

app_name = 'BookLoan'

urlpatterns = [
    path('', views.newLoan, name = 'newLoan'),
]
