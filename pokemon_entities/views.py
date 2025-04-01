import folium
import json

from django.http import HttpResponseNotFound, HttpRequest
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity
from django.utils.timezone import localtime, datetime
from pytz import timezone


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(appeared_at__lt=localtime(timezone=timezone('Europe/Moscow')), disappeared_at__gt=localtime(timezone=timezone('Europe/Moscow'))):
        image_path = pokemon_entity.pokemon.image
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(image_path.url) if image_path else DEFAULT_IMAGE_URL
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL,
            'title_ru': pokemon.title_ru,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemon_entity = PokemonEntity.objects.get(id=pokemon_id)
    except:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    pokemon = pokemon_entity.pokemon
    next_evolution = pokemon.next_evolution.first()
    image_path = pokemon.image
    image_uri = request.build_absolute_uri(image_path.url) if image_path else DEFAULT_IMAGE_URL
    pokemon_data = {
        'title_ru': pokemon.title_ru,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'img_url': image_uri,
        'entities': [
            {
                "level": int,
                "lat": int,
                "lon": int
            }
            ],

        'next_evolution': {
            'pokemon_id': next_evolution.id,
            'title_ru': next_evolution.title_ru,
            'img_url': request.build_absolute_uri(next_evolution.image.url) if next_evolution.image else DEFAULT_IMAGE_URL
        } if next_evolution else None,

        'previous_evolution': {
            'pokemon_id': pokemon.evolved_from.id,
            'title_ru': pokemon.evolved_from.title_ru,
            'img_url': request.build_absolute_uri(pokemon.evolved_from.image.url) if pokemon.evolved_from.image else DEFAULT_IMAGE_URL
        } if pokemon.evolved_from else None,
                    }
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    add_pokemon(
        folium_map, pokemon_entity.lat,
        pokemon_entity.lon,
        image_uri
    )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_data
    })
