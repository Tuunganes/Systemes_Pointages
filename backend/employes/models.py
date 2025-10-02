from django.db import models

class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20, unique=True)
    poste = models.CharField(max_length=100, blank=True)
    structure = models.CharField(max_length=100, blank=True)
    site = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    date_engagement = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"