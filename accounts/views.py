from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # authenticate user
        user = authenticate(request, username=username, password=password)
        # if authentication failed, show error, return to login page
        if user is None:
            context = {
                "error" : "Invalid username or password."
            }
            return render(request, "accounts/login.html", context=context)

        # log user in
        login(request, user)
        return redirect("/")

    context = {}

    return render(request, "accounts/login.html", context=context)


def logout_view(request):

    context = {}

    return render(request, "accounts/logout.html", context=context)


def register_view(request):

    context = {}

    return render(request, "accounts/register.html", context=context)