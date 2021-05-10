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

WAD | Group 21
