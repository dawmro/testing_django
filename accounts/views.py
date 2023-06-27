from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        # validate form
        if form.is_valid():
            user = form.get_user()
            # log user in
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context=context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")

    context = {}

    return render(request, "accounts/logout.html", context=context)


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login")

    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context=context)