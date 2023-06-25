from django.shortcuts import render

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

    context = {}

    return render(request, "accounts/login.html", context=context)


def logout_view(request):

    context = {}

    return render(request, "accounts/logout.html", context=context)


def register_view(request):

    context = {}

    return render(request, "accounts/register.html", context=context)