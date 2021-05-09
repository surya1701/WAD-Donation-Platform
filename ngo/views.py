from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from donor.models import Users, Donations, Causes
from django.core.files.storage import FileSystemStorage
# Create your views here.


def index(request):
    # NGO homes page, handles login, display causes for respective logged in NGO
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
    # Form to edit, delete & add causes
    if request.user.is_authenticated:
        if request.user.first_name == "NGO":
            if request.method == "POST":
                c = request.GET.get("c")
                cause = request.POST.get("cause")
                amt_req = request.POST.get("amt-req")
                image = request.FILES.get('img')
                if image != None:
                    fs = FileSystemStorage()
                    image = fs.save(image.name, image)
                    image = fs.url(image)
                # Adding only a new cause
                if c == "add":
                    if Causes.objects.filter(cause=cause, ngo_name=request.user.username).exists():
                        messages.error(request, "Cause already exists")
                        return render(request, "edit-cause.html", {"cause": "add"})
                    else:
                        new_cause = Causes(
                            cause=cause, ngo_name=request.user.username, amount_req=amt_req, image=image)
                        new_cause.save()
                else:
                    # Editing existing cause
                    new_cause = Causes.objects.get(
                        cause=cause, ngo_name=request.user.username)
                    # Deleting existing cause
                    if "delete" in request.POST:
                        new_cause.delete()
                    else:
                        new_cause.cause = cause
                        new_cause.amount_req = amt_req
                        if image != None:
                            new_cause.image = image
                        new_cause.save()
                return redirect("ngo")

            else:
                c = request.GET.get("c")
                # Check if cause is in database
                if c != "add":
                    if not Causes.objects.filter(cause=c, ngo_name=request.user.username).exists():
                        return redirect("ngo")
                    return render(request, "edit-cause.html", {"cause": Causes.objects.get(cause=c, ngo_name=request.user.username)})
                elif c == "add":
                    return render(request, "edit-cause.html", {"cause": "add"})
                return redirect("ngo")
        else:
            return redirect("index")
    else:
        return redirect("index")


def donations(request):
    # List donations for specififc cause
    if request.user.is_authenticated:
        if request.user.first_name == "NGO":
            cause = request.GET.get('c')
            if Donations.objects.filter(cause_id=Causes.objects.get(cause=cause, ngo_name=request.user.username)).exists():
                donations = Donations.objects.filter(cause_id=Causes.objects.get(
                    cause=cause, ngo_name=request.user.username))
                return render(request, "donations.html", {"donations": donations, "cause": cause})
            else:
                messages.error(request, "No Donations")
    return redirect("ngo")


def logout(request):
    auth.logout(request)
    return redirect("ngo")
