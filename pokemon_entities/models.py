from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True)
    description = models.CharField(max_length=1000, blank=True)

    evolved_from = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='next_evolution'
    )

    def __str__(self):
        return self.title_ru

    

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
