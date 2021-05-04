from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('causes', views.causes, name="causes"),
    path('contact', views.contact, name="contact"),
    path('donate', views.donate, name="donate"),
    path('success', views.success, name="success"),
    path('success_mail', views.success_mail, name="success_mail"),
    path('logout', views.logout, name="logout"),
    path('accounts/', include('allauth.urls')),
]

# aa
