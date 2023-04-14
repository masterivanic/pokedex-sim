import django_filters

from .models import PokedexCreature


class PokedexCreatureFilter(django_filters.FilterSet):
    """Filters for pokedex creature listing"""

    type_1 = django_filters.CharFilter(field_name="type_1", lookup_expr="iexact")
    type_2 = django_filters.CharFilter(field_name="type_2", lookup_expr="iexact")
    generation = django_filters.NumberFilter(lookup_expr="in")
    legendary = django_filters.BooleanFilter(
        field_name="legendary", method="filter_by_legendary"
    )

    def filter_by_legendary(self, queryset, name, value):
        # construct the full lookup expression.
        lookup = "__".join([name, "isnull"])
        return queryset.filter(**{lookup: False})

    class Meta:
        model = PokedexCreature
        fields = ["type_1", "type_2", "generation", "legendary"]
