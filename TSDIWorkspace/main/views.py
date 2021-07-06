from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Testing, Lease, Bill, ServiceRequest, MailAndPackage, Notification

# Create your views here.


def index(request):
    return render(request, "main/index.html")



def workspace(request):
    return render(request, "main/workspace.html")



def loginView(request):

    if request.method == "POST":

        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to portal:
        if user:
            login(request, user)
            return render(request, "main/portal.html")
        # Otherwise, return login page again with new context
        else:
            return render(request, "main/login.html", {
                "message": "Invalid Credentials"
            })

    if request.user.is_authenticated:
        return render(request, "main/portal.html")

    return render(request, "main/login.html")



def logoutView(request):
    logout(request)
    return render(request, "main/login.html", {
        "message": "Logged Out"
    })



def myLeases(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "main/my_leases.html", {
        "leases": Lease.objects.filter(lessee=request.user)
    })



def bills(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "main/bills.html", {
        "bills": Bill.objects.filter(lessee=request.user)
    })



def serviceRequests(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "main/service_requests.html", {
        "serviceRequests": ServiceRequest.objects.filter(lessee=request.user)
    })



def mailsAndPackages(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "main/mails_and_packages.html", {
        "mailsAndPackages": MailAndPackage.objects.filter(lessee=request.user)
    })



def notifications(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "main/notifications.html")



def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "main/profile.html")




