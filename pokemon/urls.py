from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet

app_name = "pokemon application"

router = DefaultRouter()
router.register("", PokemonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
