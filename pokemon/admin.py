from django.contrib import admin

from pokemon.models import Pokemon


class PokemonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pokemon._meta.fields]
    search_fields = ("nickname", "trainer_id__username")
    list_per_page = 50

    autocomplete_fields = ("pokedex_creature_id", "trainer_id")


admin.site.register(Pokemon, PokemonAdmin)

admin.site.site_header = "POKEDEX Admin"
admin.site.site_title = "POKEDEX Admin Portal"
admin.site.index_title = "Welcome to POKEDEX Portal"
