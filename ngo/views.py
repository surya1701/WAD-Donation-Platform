from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if request.user.first_name == "NGO":
            return render(request, "ngo.html")
        else:
            return redirect("index")
    else:
        if request.method == "POST":
            name = request.POST['name']
            pas = request.POST['password']
            ngo = auth.authenticate(
                username=name, password=pas, first_name="NGO")
            if ngo:
                auth.login(request, ngo)
                print(ngo.is_authenticated)
                return render(request, "ngo.html")
            else:
                messages.error(request, "Name or Passsword is incorrect")
                return render(request, "ngo.html")
        else:
            return render(request, "ngo.html")


def logout(request):
    auth.logout(request)
    return redirect("ngo")
