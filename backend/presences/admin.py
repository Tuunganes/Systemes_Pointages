from django.contrib import admin
from .models import Presence
from historique.models import Historique

@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ('employe', 'date_presence', 'heure_entree', 'heure_sortie')
    list_filter = ('date_presence', 'employe')
    search_fields = ('employe__nom', 'employe__prenom')

    def save_model(self, request, obj, form, change):
        action = "Modification présence" if change else "Création présence"
        super().save_model(request, obj, form, change)
        # on construit une chaîne descriptive
        employe_info = f"{obj.employe.nom} {obj.employe.prenom}" if obj.employe else "Employé supprimé"
        Historique.objects.create(
            utilisateur=request.user,
            action=f"{action}: {employe_info} à {obj.date_presence}"
        )