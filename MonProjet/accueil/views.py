from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def helloWorld(self):
    html = "<h1>Hello World !</h1>"
    return HttpResponse(html)

def helloWorldWithTemplate(requests):
    return render(requests, "helloWorld.html", {'date':datetime.datetime.now(),})

def sum(requests,n1,n2):
    return render(requests, "sum.html", {'somme':int(n1)+int(n2)})

def sumTemplate(requests,n1,n2):
    return render(requests, "sum.html", {'n1':int(n1),'n2':int(n2)})
