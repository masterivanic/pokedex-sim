from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PokemonCreatureViewSet

app_name = "pokedex application"

router = DefaultRouter()
router.register("", PokemonCreatureViewSet, basename="pokedex")


urlpatterns = [
    path("", include(router.urls)),
]
