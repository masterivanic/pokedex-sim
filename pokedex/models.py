from django.db import models

# Create your models here.

class PokedexCreature(models.Model):
    """ define a pokedex """

    name = models.CharField(max_length=100, blank=False, unique=True)
    type_1 = models.CharField(max_length=100, blank=False, null=False)
    type_2 = models.CharField(max_length=100, blank=False, null=False)
    total = models.PositiveSmallIntegerField()
    hp = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    sp_atk = models.PositiveSmallIntegerField()
    sp_def = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    generation = models.PositiveSmallIntegerField()
    legendary = models.BooleanField(blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

   
