from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Название(рус.)')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Название(анг.)')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Название(яп.)')
    image = models.ImageField(null=True, verbose_name='Изображение', upload_to='pokemon_image')
    description = models.TextField(blank=True, verbose_name='Описание')

    evolved_from = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='next_evolutions',
        verbose_name='Из кого эволюционировал'
    )

    def __str__(self):
        return self.title_ru

    

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон', related_name='entities')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=now, null=True, blank=True, verbose_name='Когда появился(тся)')
    disappeared_at = models.DateTimeField(default=now, null=True, blank=True, verbose_name='Когда пропадет(ал)')
    level = models.PositiveIntegerField(null=True, verbose_name='Уровень')
    health = models.PositiveIntegerField(null=True, verbose_name='Здоровье')
    strength = models.PositiveIntegerField(null=True, verbose_name='Сила')
    defence = models.PositiveIntegerField(null=True, verbose_name='Защита')
    stamina = models.PositiveIntegerField(null=True, verbose_name='Выносливость')
