from rest_framework import serializers

from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    """Serializer of Pokemon object"""

    class Meta:
        model = Pokemon
        fields = (
            "pokedex_creature_id",
            "trainer_id",
            "nickname",
            "level",
            "experience",
        )
        read_only_fields = ("id", "level")

    def validate(self, attrs):
        """Add pokemon nickname if no nickname is given"""

        nickname = attrs.get("nickname")
        pokedex_creature = attrs.get("pokedex_creature_id")
        if not nickname:
            attrs["nickname"] = pokedex_creature.name

        return super().validate(attrs)


class PokemonGiveXPSerializer(serializers.Serializer):
    """Serializer of give-xp endpoint"""

    amount = serializers.IntegerField(min_value=0)
