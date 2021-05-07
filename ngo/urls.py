from django.urls import path, include
from . import views

urlpatterns = [
    path('ngo', views.index, name="ngo"),
    path('edit', views.edit, name="edit"),
    path('donations', views.donations, name="donations"),
    path('ngo-logout', views.logout, name="ngo-logout")
]

# aa
