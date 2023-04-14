from rest_framework import viewsets

from .filters import PokedexCreatureFilter
from .pokedex_repo import PokedexRepository
from .serializers import PokedexCreatureDetailSerializer
from .serializers import PokedexCreatureSerializer


class PokemonCreatureViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint to display all Pokedex Creatures"""

    queryset = PokedexRepository.get_all_pokedex()
    serializer_class = PokedexCreatureSerializer
    filterset_class = PokedexCreatureFilter

    def get_serializer_class(self):
        """Return appropriate serializer class"""

        if self.action == "retrieve":
            return PokedexCreatureDetailSerializer
        return self.serializer_class
