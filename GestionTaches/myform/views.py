from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django import forms
from django.shortcuts import render
from django.forms import ModelForm
from myform.models import Contact
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email', 'message')

class ContactForm2(forms.Form):
    name = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(max_length=1000)

def contact(request):
    contact_form = ContactForm()
    return render(request,'contact.html', {'contact_form' : contact_form})
    # return HttpResponse('bienvenue sur contact')

def contact2(request):
    contact_form2 = ContactForm2()
    return render(request,'contact.html', {'contact_form' : contact_form2})