from django.urls import path, include
from . import views

urlpatterns = [
    path('ngo', views.index, name="ngo"),
    path('ngo-logout', views.logout, name="ngo-logout")
]

# aa
