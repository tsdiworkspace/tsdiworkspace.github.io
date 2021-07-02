from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout")
]
