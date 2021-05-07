from django.shortcuts import render, redirect
from donor.models import Users, Donations, Causes
import razorpay
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from donor.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import random

from django.template.loader import render_to_string

# Create your views here.


def get_user(request):
    if request.user.is_authenticated:
        donation = Donations.objects.filter(paid=False)
        donation.delete()
        if not Users.objects.filter(email=request.user.email).exists():
            u = Users(email=request.user.email)
            u.save()
        u = Users.objects.get(email=request.user.email)
        print(u.pk)
        donations = Donations.objects.filter(user_id=u)
        u_dict = {'email': u.email, 'amt': u.total_amt,
                  'since': u.since, 'id': u.pk, 'donations': donations}
    return u_dict


def index(request):
    if request.user.is_authenticated:
        u_dict = get_user(request)
        causes = list(Causes.objects.all())
        tot_don = sum([i.amount_donated for i in causes])
        tot_req = sum([i.amount_req for i in causes])
        u_dict["tot_don"] = tot_don
        u_dict["tot_req"] = tot_req
        if len(causes) == 0:
            return render(request, "index.html", u_dict)
        count = min([len(causes), 3])
        causes = random.sample(causes, count)
        u_dict["causes"] = causes
        return render(request, "index.html", u_dict)
    else:
        al = Users.objects.filter(total_amt=0)
        causes = list(Causes.objects.all())
        tot_don = sum([i.amount_donated for i in causes])
        tot_req = sum([i.amount_req for i in causes])
        if len(causes) == 0:
            return render(request, "index.html", {'all': al, 'tot_don': tot_don, 'tot_req': tot_req})
        count = min([len(causes), 3])
        causes = random.sample(causes, count)
        return render(request, "index.html", {'all': al, "causes": causes, 'tot_don': tot_don, 'tot_req': tot_req})


def about(request):
    if request.user.is_authenticated:
        u_dict = get_user(request)
        return render(request, "about.html", u_dict)
    else:
        return render(request, "about.html")


def causes(request):
    if request.user.is_authenticated:
        u_dict = get_user(request)
        causes = list(Causes.objects.all())
        random.shuffle(causes)
        u_dict["causes"] = causes
        return render(request, "causes.html", u_dict)
    else:
        causes = list(Causes.objects.all())
        random.shuffle(causes)
        return render(request, "causes.html", {"causes": causes})


def donate(request):
    if request.method == "POST" and request.user.is_authenticated:
        amount = int(request.POST.get("amount"))*100
        cause = request.POST.get("cause")
        ngo = request.POST.get("ngo")
        client = razorpay.Client(
            auth=("rzp_test_GsYLne4Fqnrf4m", "5FbYXB3Lhc3MO9e9d9GNgEmY"))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
        u_dict = get_user(request)
        user_id = Users.objects.get(pk=u_dict['id'])
        cause_id = Causes.objects.get(cause=cause, ngo_name=ngo)
        donation = Donations(cause_id=cause_id, user_id=user_id,
                             amount=amount/100, razorpay_id=payment['id'])
        donation.save()
        u_dict['payment'] = payment
        u_dict['cause'] = cause
        u_dict['ngo'] = ngo
        return render(request, "donate.html", u_dict)
    if request.user.is_authenticated:
        u_dict = get_user(request)
        u_dict['cause'] = request.GET.get('c')
        u_dict['ngo'] = request.GET.get('n')
        if u_dict['cause'] == None or u_dict['ngo'] == None or not Causes.objects.filter(cause=u_dict['cause'], ngo_name=u_dict['ngo']).exists():
            return redirect("causes")
        return render(request, "donate.html", u_dict)
    else:
        return redirect("causes")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Mail received"
            name = request.POST.get('first_name') + \
                " " + request.POST.get('second_name')
            email = request.POST.get('email_address')
            message = request.POST.get('message')
            message = "Name: "+name + "\nMessage: " + message
            print(message)
            send_mail(subject, message, email, [
                'dude05422@gmail.com', ], fail_silently=False,)
            return redirect("/")
        else:
            messages.error(request, "Invalid Submission")
            return redirect("contact")
    form = ContactForm()
    if request.user.is_authenticated:
        u_dict = get_user(request)
        u_dict["form"] = form
        return render(request, "contact.html", u_dict)
    else:
        return render(request, "contact.html", {'form': form})


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        print(a)
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
        donation = Donations.objects.get(razorpay_id=order_id)
        if donation.paid == False:
            donation.paid = True
            user = donation.user_id
            user.total_amt += donation.amount
            cause = donation.cause_id
            cause.amount_donated += donation.amount
            donation.save()
            user.save()
            cause.save()
        u_dict = get_user(request)
        u_dict["order"] = order_id
        return render(request, "success.html", u_dict)
    return redirect("causes")


def success_mail(request):
    if request.method == "POST":
        order_id = request.POST.get("order")
        donation = Donations.objects.get(razorpay_id=order_id)
        user = donation.user_id
        cause = donation.cause_id
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string(
            'email.html', {"cause": cause.cause, "amt": donation.amount, "order": order_id})
        send_mail("Your donation has been received.", msg_plain, settings.EMAIL_HOST_USER,
                  [user.email, ], html_message=msg_html, fail_silently=False, )
    return redirect("/")


def logout(request):
    return render(request, "logout.html")
