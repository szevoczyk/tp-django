
from django.contrib import admin
from django.urls import path, include
from .views import mylist,showcontact

urlpatterns = [
    path('',mylist,name="list"),
    path('contact/<str:nom>/<str:prenom>/<str:telephone>/',showcontact,name="contact"),
]