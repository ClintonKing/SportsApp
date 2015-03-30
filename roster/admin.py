from django.contrib import admin
from roster.models import Team, Player
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
