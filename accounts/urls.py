# users/urls.py
from django.urls import path
from .views import login_or_register

urlpatterns = [
    path("auth/", login_or_register),
]
