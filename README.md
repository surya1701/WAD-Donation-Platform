# Donation Platform &copy;
This application has been designed by GROUP 21, as a semester project for WEB APPLICATION DEVELOPMENT course.

## Contents
<ul> 
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#installation">Installation</a>
    <ul>
        <li><a href="#sqlite3">With SQLITE3</a></li>
        <li><a href="#postgresql">With PostgreSQL</a></li>
    </ul>
    </li>
    <li><a href="#code">Code Snippets</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#contributors">Contributors</a></li>
    <li><a href="#deployed-website">Deployed Website</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
   </ul>

## Introduction
This project has three modules namely, Admin, NGO and Donor.
Admin can login as a super-user and manage the requests raised by NGOs. The NGO will be added to the system after verifying the documents sent by the them via the contact page.
Once approved, NGOs can login to the NGO module/app and view the interface. This page displays a table of all their causes and donations, where they can add, edit and delete their causes.
Donors can simply register and login using their google credentials. They can decide to donate to any of the causes added by the NGOs. The digital payment is hassle free, secure and includes many payment options, thanks to the Razorpay API. Donors will get an email confirmation and their user profile will show all their donations with the respective cause name and amount.

## Installation
After [cloning](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) the repo.
```console
foo@bar:~$ pip install -r requirements.txt
```
### SQLITE3
```console
foo@bar:~$ foo@bar:~$ python manage.py runserver
```
### PostgreSQL
Setup your [postgresql account](https://pynative.com/python-postgresql-tutorial/#:~:text=Install%20Psycopg2%20using%20the%20pip%20command&text=This%20module%20is%20available%20on,pip%20command%20to%20install%20Psycopg2.&text=You%20can%20also%20install%20a%20specific%20version%20using%20the%20following%20command.).

Add your details to charity > settings.py :
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'donationplatform',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': 'localhost'
    }
}
```
```console
foo@bar:~$ python manage.py collectstatic
foo@bar:~$ python manage.py makemigrations
foo@bar:~$ python manage.py migrate
foo@bar:~$ python manage.py runserver
```
You're all set to go.

Note: sqlite3 file contains a pre-filled database, whereas, if you setup postgres, the superuser, ngos and causes must be added.


## Code

```
def get_user(request):
    # Sends logged in user's data
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
 ```
 The above function helps to fetch the details of the logged in donor from database and return it as a dictonary.
 
 ```
     if request.method == "POST" and request.user.is_authenticated:
        # because razorpay handles in paisa
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
        donation = Donations(cause_name=cause, cause_id=cause_id, user_id=user_id,
                             amount=amount/100, razorpay_id=payment['id'])
        donation.save()
        u_dict['payment'] = payment
        u_dict['cause'] = cause
        u_dict['ngo'] = ngo
        return render(request, "donate.html", u_dict)
```
The above code fetches the data about the donor when he/she donates for a particular cause. This data is further used for sending the confirmation mail with payment id to the donor.

```
#function to send confirmation mail to donor
 msg_plain = render_to_string('email.txt')
 msg_html = render_to_string('email.html', {"cause": cause.cause, "amt": donation.amount, "order": order_id})
        send_mail("Your donation has been received.", msg_plain, settings.EMAIL_HOST_USER,
                  [user.email, ], html_message=msg_html, fail_silently=False, )
```                 
```
# Application definition in settings.py

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dude05422@gmail.com'
EMAIL_HOST_PASSWORD = 'ujhbteodtzbfiycx'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

```
The above two sections of code are used for sending confrimation mail to the donor.

```
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

```
The above code segment is used to send a confirmation mail to a NGO, when it contacts the admin for NGO registraion.

```

# NGO homes page, handles login, display causes for respective logged in NGO
    if request.user.is_authenticated:
        if request.user.first_name == "NGO":
            causes = Causes.objects.filter(ngo_name=request.user.username)
            return render(request, "ngo.html", {"causes": causes})
        else:
            return redirect("index")
```
The above code segment is for NGO module, when any NGO logs in.

The below section is for **Database** .
```

# Database modal for user
class Users(models.Model):
    email = models.EmailField()
    total_amt = models.PositiveIntegerField(default=0)
    since = models.DateTimeField(auto_now_add=True)

# Database model for Causes added and edited by NGO's
class Causes(models.Model):
    cause = models.CharField(max_length=50)
    ngo_name = models.CharField(max_length=50)
    amount_req = models.PositiveIntegerField()
    amount_donated = models.PositiveIntegerField(default=0)
    image = models.URLField(default="static/images/index/img-4.jpg")

# Database model for donors which contains payment id,user id etc.
class Donations(models.Model):
    cause_name = models.CharField(max_length=50)
    cause_id = models.ForeignKey(Causes, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField()
    razorpay_id = models.CharField(unique=True, max_length=50)
    paid = models.BooleanField(default=False)

```

The above code section is database description. As we have earlier mentioned, our projects consists of three modules- Admin, NGO and Donor . And here are the three databases for them respectively.


## Screenshots

<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD1.PNG">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD3.PNG">
<p float="left">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD6.PNG" width="400" height="580">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD13.PNG" width="400" height="580">
</p>
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD7.PNG">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD9.PNG">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD10.PNG">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD11.PNG">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD8.PNG">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD12.PNG">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD14.PNG">
<img src="https://github.com/piyush9311/WAD-Donation-Platform/blob/main/static/images/screenshots/WAD15.PNG">

## Contributors
[Piyush Kumar](https://github.com/piyush9311)<br>
[S Suryavardan](https://github.com/surya1701)<br>
[Anurag Kumar](https://github.com/anu725053)<br>
[Himesh Kumar](https://github.com/Himesh18)<br>
[Chaintany Anand Kopoori](https://github.com/chaitanya9993)<br>

## Deployed Website
[Deployed Website](https://donationplatform-wad.herokuapp.com/)
The project has been deployed on Heroku, with sqlite3.

## Tech Stack
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>

**WAD | Group 21**
