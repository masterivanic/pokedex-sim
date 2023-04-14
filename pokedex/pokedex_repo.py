from .models import PokedexCreature


class PokedexRepoHandler:
    """An abstraction layer for access data"""

    @staticmethod
    def get_all_pokedex():
        """
        Get all pokedex

        :return: a queryset object list of pokedex
        """
        raise NotImplementedError


class PokedexRepository(PokedexRepoHandler):
    """define a repository query db"""

    @staticmethod
    def get_all_pokedex():
        query = PokedexCreature.objects.all()
        return query
