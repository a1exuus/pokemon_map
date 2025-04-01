from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, blank=True, verbose_name='Название(рус.)')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Название(анг.)')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Название(яп.)')
    image = models.ImageField(null=True, verbose_name='Изображение')
    description = models.CharField(max_length=1000, blank=True, verbose_name='Описание')

    evolved_from = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='next_evolution',
        verbose_name='Из кого эволюционировал'
    )

    def __str__(self):
        return self.title_ru

    

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=now, verbose_name='Когда появился')
    disappeared_at = models.DateTimeField(default=now, verbose_name='Когда пропадет(ал)')
    level = models.IntegerField(default=3, verbose_name='Уровень')
    health = models.IntegerField(default=3, verbose_name='Здоровье')
    strength = models.IntegerField(default=3, verbose_name='Сила')
    defence = models.IntegerField(default=3, verbose_name='Защита')
    stamina = models.IntegerField(default=3, verbose_name='Выносливость')
