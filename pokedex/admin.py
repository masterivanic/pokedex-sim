from django.contrib import admin
from .models import PokedexCreature

# Register your models here.

@admin.register(PokedexCreature)
class PokemonCreatureAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields = ("name",)
    list_filter = ("type_1", "type_2", "generation", "legendary")




    