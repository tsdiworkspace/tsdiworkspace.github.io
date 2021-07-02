from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, "main/index.html")



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

    return render(request, "main/login.html")



def logoutView(request):
    logout(request)
    return render(request, "main/login.html", {
                "message": "Logged Out"
            })
