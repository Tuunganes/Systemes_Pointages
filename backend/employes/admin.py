from django.contrib import admin
from .models import Employe
from historique.models import Historique

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'matricule', 'date_engagement')
    search_fields = ('nom', 'prenom', 'matricule')
    list_filter = ('date_engagement',)

    def save_model(self, request, obj, form, change):
        # change == True si modification d’un objet existant, False si création
        action = "Modification employé" if change else "Création employé"
        super().save_model(request, obj, form, change)
        Historique.objects.create(
            utilisateur=request.user,
            action=f"{action}: {obj.matricule} - {obj.nom} {obj.prenom}"
        )