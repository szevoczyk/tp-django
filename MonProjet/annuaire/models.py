from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    nom = models.CharField(max_length=25)
    entreprise = models.BooleanField(default=False)