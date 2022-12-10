
from django.contrib import admin
from django.urls import path, include
from .views import mylist,showcontact

urlpatterns = [
    path('<str:typeAnnuaire>/',mylist,name="list"),
    path('contactBlanche/<str:nom>/<str:prenom>/<str:telephone>/',showcontact,name="contact"),
    path('contactJaune/<str:nom>/<str:telephone>/',showcontact,name="contact"),
]