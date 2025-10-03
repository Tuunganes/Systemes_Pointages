from django.contrib import admin
from .models import Historique

@admin.register(Historique)
class HistoriqueAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'action', 'date_action')
    list_filter = ('date_action', 'utilisateur')
    search_fields = ('action', 'utilisateur__username')
    readonly_fields = ('date_action',)