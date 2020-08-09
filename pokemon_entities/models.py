from django.db import models

# your models here


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.TextField()
    photo = models.ImageField(null=True)
    description = models.TextField(blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    
    # Relationships
    previous_evolution = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_evolutions')

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)

    # Relationships
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, related_name='pokemon_entities')

    lat = models.FloatField()
    lon = models.FloatField()

    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)

    level = models.IntegerField(default=None)
    health = models.IntegerField(default=None)
    strength = models.IntegerField(default=None)
    defence = models.IntegerField(default=None)
    stamina = models.IntegerField(default=None)
