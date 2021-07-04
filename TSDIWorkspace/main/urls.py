from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("workspace", views.workspace, name="workspace"), 
    path("login", views.loginView, name="login"), 
    path("logout", views.logoutView, name="logout"),
    path("my_lease", views.myLease, name="myLease"),
    path("bills", views.bills, name="bills"),
    path("service_requests", views.serviceRequests, name="serviceRequests"),
    path("mails_and_packages", views.mailsAndPackages, name="mailsAndPackages"),
    path("notifications", views.notifications, name="notifications"),
    path("profile", views.profile, name="profile"),
]
