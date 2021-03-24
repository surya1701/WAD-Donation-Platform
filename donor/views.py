from django.shortcuts import render
from donor.models import Users


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if not Users.objects.filter(email=request.user.email).exists():
            u = Users(email=request.user.email)
            u.save()
        u = Users.objects.get(email=request.user.email)
        u_dict = {'email': u.email, 'amt': u.total_amt}
        print(u.pk)
        return render(request, "index.html", u_dict)
    else:
        return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def logout(request):
    return render(request, "logout.html")
