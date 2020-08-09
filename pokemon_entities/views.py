import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def get_image_url_or_default(request, path_to_search_image):
    try:
        img_url = request.build_absolute_uri(path_to_search_image.url)
    except Exception:
        img_url = DEFAULT_IMAGE_URL
    return img_url


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    pokemon_entities = PokemonEntity.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:

        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon.title,
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url))

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()

    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.photo.url if pokemon.photo else None,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    try:
        requested_pokemon = Pokemon.objects.get(id=int(pokemon_id))
    except Exception:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')


    img_url = get_image_url_or_default(request, requested_pokemon.photo)


    print(50*'-')
    print(requested_pokemon)
    print(50*'-')



    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemon.pokemon_entities.all():
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            requested_pokemon.title, img_url)

    pokemon = {
        'title_ru': requested_pokemon.title,
        'img_url': img_url,
    }


    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})
