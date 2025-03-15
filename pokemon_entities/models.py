from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return '{}'.format(self.title)
    

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=now)
    disappeared_at = models.DateTimeField(default=now)
    level = models.IntegerField(default=3)
    health = models.IntegerField(default=3)
    strength = models.IntegerField(default=3)
    defence = models.IntegerField(default=3)
    stamina = models.IntegerField(default=3)
