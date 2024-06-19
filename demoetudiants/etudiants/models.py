from django.db import models

# Create your models here.

class Etudiants(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
