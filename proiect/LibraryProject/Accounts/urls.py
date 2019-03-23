from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signupView, name = 'signup'),
    path('login', views.loginView, name = 'login'),
    path('logut', views.logoutView, name = "logout"),
]