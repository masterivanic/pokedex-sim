from rest_framework import serializers

from .models import PokedexCreature


class PokedexCreatureSerializer(serializers.ModelSerializer):
    """Serializer of PokedexCreature object"""

    class Meta:
        model = PokedexCreature
        fields = (
            "id",
            "name",
            "type_1",
            "type_2",
            "generation",
            "legendary",
        )
        read_only_fields = ("id",)


class PokedexCreatureDetailSerializer(serializers.ModelSerializer):
    """Serializer of PokedexCreature object with more details"""

    class Meta:
        model = PokedexCreature
        fields = "__all__"
        read_only_fields = ("id",)
