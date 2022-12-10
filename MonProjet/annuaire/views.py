from django.shortcuts import render
from .models import Contact

def mylist(requests,typeAnnuaire):
  if typeAnnuaire== "particuliers":
    entreprise=False
    template = "listBlanche.html"
  if typeAnnuaire== "entreprises":
    entreprise=True
    template = "listJaune.html"
  contacts = Contact.objects.filter(entreprise=entreprise).all()
  return render(requests, template,{'data':contacts})   

def showcontact(requests,nom,telephone,prenom=""):
  return render(requests, "contact.html",{'nom':nom,'prenom':prenom,'telephone':telephone})
