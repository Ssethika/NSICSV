from webbrowser import Error
import requests

def get_pokemon_info(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.strip().lower()}"

    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
    else:
        raise Error
    print(response)
    return response

def get_pokemon_sprite(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.strip().lower()}"

    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
    else:
        raise Error

    return str(response["sprites"]["front_default"])

def get_pokemon_description(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{name.strip().lower()}"

    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
    else:
        raise Error

    return str(response["flavor_text_entries"][0]["flavor_text"])