from django.shortcuts import render, redirect
from donor.models import Users


# Create your views here.
def get_user(request):
    if request.user.is_authenticated:
        if not Users.objects.filter(email=request.user.email).exists():
            u = Users(email=request.user.email)
            u.save()
        u = Users.objects.get(email=request.user.email)
        print(u.pk)
        u_dict = {'email': u.email, 'amt': u.total_amt, 'since': u.since}
    return u_dict


def index(request):
    if request.user.is_authenticated:
        u_dict = get_user(request)
        return render(request, "index.html", u_dict)
    else:
        al = Users.objects.filter(total_amt=0)
        return render(request, "index.html", {'all': al})


def about(request):
    if request.user.is_authenticated:
        u_dict = get_user(request)
        return render(request, "about.html", u_dict)
    else:
        return render(request, "about.html")


def causes(request):
    if request.user.is_authenticated:
        u_dict = get_user(request)
        return render(request, "causes.html", u_dict)
    else:
        return render(request, "causes.html")


def donate(request):
    if request.user.is_authenticated:
        u_dict = get_user(request)
        u_dict['cause'] = request.GET.get('c')
        u_dict['ngo'] = request.GET.get('n')
        if u_dict['cause'] == None or u_dict['ngo'] == None:
            # check if cause in database **important
            return redirect("causes")
        return render(request, "donate.html", u_dict)
    else:
        return redirect("causes")
        # return render(request, "donate.html")


def logout(request):
    return render(request, "logout.html")
