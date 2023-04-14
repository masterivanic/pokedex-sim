from .models import Pokemon


class PokemonRepoHandler:
    """An abstraction layer for access data"""

    @staticmethod
    def get_all_pokemon():
        """
        Get all pokemon

        :return: a queryset object list of pokemon
        """
        raise NotImplementedError


class PokemonRepository(PokemonRepoHandler):
    @staticmethod
    def get_all_pokemon():
        query = Pokemon.objects.all()
        return query
