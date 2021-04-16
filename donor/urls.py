from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('causes', views.causes, name="causes"),
    path('donate', views.donate, name="donate"),
    path('logout', views.logout, name="logout"),
    path('accounts/', include('allauth.urls')),
]

# aa
