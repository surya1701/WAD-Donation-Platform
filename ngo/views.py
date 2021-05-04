from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from donor.models import Users, Donations, Causes
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if request.user.first_name == "NGO":
            causes = Causes.objects.filter(ngo_name=request.user.username)
            return render(request, "ngo.html", {"causes": causes})
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
                return redirect("ngo")
            else:
                messages.error(request, "Name or Passsword is incorrect")
                return render(request, "ngo.html")
        else:
            return render(request, "ngo.html")


def edit(request):
    if request.user.is_authenticated:
        if request.user.first_name == "NGO":
            if request.method == "POST":
                c = request.GET.get("c")
                cause = request.POST.get("cause")
                amt_req = request.POST.get("amt-req")
                if c == "add":
                    if Causes.objects.filter(cause=cause).exists():
                        messages.error(request, "Cause already exists")
                        return render(request, "edit-cause.html", {"cause": "add"})
                    else:
                        new_cause = Causes(
                            cause=cause, ngo_name=request.user.username, amount_req=amt_req)
                        new_cause.save()
                else:
                    new_cause = Causes.objects.get(cause=cause)
                    new_cause.cause = cause
                    new_cause.amount_req = amt_req
                    new_cause.save()
                return redirect("ngo")

            else:
                c = request.GET.get("c")
                if c != "add":
                    if not Causes.objects.filter(cause=c).exists():
                        return redirect("ngo")
                    return render(request, "edit-cause.html", {"cause": Causes.objects.get(cause=c)})
                elif c == "add":
                    return render(request, "edit-cause.html", {"cause": "add"})
                return redirect("ngo")
        else:
            return redirect("index")
    else:
        return redirect("index")


def logout(request):
    auth.logout(request)
    return redirect("ngo")
