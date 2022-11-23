
from django.contrib import admin
from django.urls import path, include
from .views import mylist

urlpatterns = [
    path('',mylist,name="list"),
]