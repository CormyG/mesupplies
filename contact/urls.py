from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.contact, name="contact")
]