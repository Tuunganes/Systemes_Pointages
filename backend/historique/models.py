from django.db import models
from django.conf import settings

class Historique(models.Model):
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='historiques'
    )
    action = models.TextField()
    date_action = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user = self.utilisateur.username if self.utilisateur else "Utilisateur supprimé"
        return f"{user} — {self.action[:60]} — {self.date_action:%Y-%m-%d %H:%M}"
    
    class Meta:
        ordering = ['-date_action']
        verbose_name = "Historique"
        verbose_name_plural = "Historiques"