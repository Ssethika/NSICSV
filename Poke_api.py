from webbrowser import Error
import requests

"""Important functions to get api information"""

def get_pokemon_info(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.strip().lower()}"


    try:
        response = requests.get(url, timeout=5)  # Set a timeout to avoid hanging
        response.raise_for_status()  # Raise an error for bad HTTP responses (4xx, 5xx)

        data = response.json()
        return data

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection or cannot reach PokeAPI.")
        return None  # Return None instead of crashing

    except requests.exceptions.Timeout:
        print("Error: Request to PokeAPI timed out.")
        return None  # Return None to avoid crashing

    except requests.exceptions.HTTPError as err:
        print(f"Error: PokeAPI returned an error - {err}")
        return None

    except requests.exceptions.RequestException as err:
        print(f"Unexpected error: {err}")
        return None

def get_pokemon_sprite(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.strip().lower()}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad HTTP responses (4xx, 5xx)

        if response.status_code == 200:
            response = response.json()
        else:
            raise Error

        return str(response["sprites"]["front_default"])

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection or cannot reach PokeAPI.")
        return None  # Return None instead of crashing

    except requests.exceptions.Timeout:
        print("Error: Request to PokeAPI timed out.")
        return None  # Return None to avoid crashing

    except requests.exceptions.HTTPError as err:
        print(f"Error: PokeAPI returned an error - {err}")
        return None

    except requests.exceptions.RequestException as err:
        print(f"Unexpected error: {err}")
        return None

def get_pokemon_description(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{name.strip().lower()}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        if response.status_code == 200:
            response = response.json()
        else:
            raise Error

        return str(response["flavor_text_entries"][0]["flavor_text"])
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection or cannot reach PokeAPI.")
        return None  # Return None instead of crashing

    except requests.exceptions.Timeout:
        print("Error: Request to PokeAPI timed out.")
        return None  # Return None to avoid crashing

    except requests.exceptions.HTTPError as err:
        print(f"Error: PokeAPI returned an error - {err}")
        return None

    except requests.exceptions.RequestException as err:
        print(f"Unexpected error: {err}")
        return None