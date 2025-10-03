from employes.models import Employe
from django.db import models

class Presence(models.Model):
    employe = models.ForeignKey(
        Employe,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='presences'
    )
    date_presence = models.DateField()
    heure_entree = models.TimeField()
    heure_sortie = models.TimeField(null=True, blank=True)
    statut = models.CharField(max_length=20, blank=True)

    def __str__(self):
       if self.employe:
        return f"{self.employe.nom} - {self.date_presence}"
       else:
        return f"Employé supprimé - {self.date_presence}"