from django.db import models


class Pokemon(models.Model):
    title = models.TextField(verbose_name='имя')
    photo = models.ImageField(null=True, verbose_name='изображение')
    description = models.TextField(blank=True, verbose_name='описание')
    title_en = models.CharField(
        max_length=200, blank=True, verbose_name='имя на английском')
    title_jp = models.CharField(
        max_length=200, blank=True, verbose_name='имя на японском')

    previous_evolution = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='next_evolutions', verbose_name='предыдущее превращение'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE,
        related_name='pokemon_entities',
        verbose_name='покемон')

    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')

    appeared_at = models.DateTimeField(
        default=None, verbose_name='появился в')
    disappeared_at = models.DateTimeField(
        default=None, verbose_name='исчез в')

    level = models.IntegerField(default=None, verbose_name='уровень')
    health = models.IntegerField(default=None, verbose_name='здоровье')
    strength = models.IntegerField(default=None, verbose_name='сила')
    defence = models.IntegerField(default=None, verbose_name='защита')
    stamina = models.IntegerField(default=None, verbose_name='выносливость')
