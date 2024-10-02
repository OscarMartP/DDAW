#Imports#
import requests
from typing import List, Optional, Dict, Any

#Metodo para obtener datos 
def fetch_data(url: str) -> Optional[Dict[str, Any]]:
    try:
        response = requests.get(url) # Peticion GET
        response.raise_for_status() # Comprobamos la solicitud
        return response.json() # Devolvemos los datos en formato JSON
    #Excepciones
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

#Metodo para obtener url tipo agua
def get_water_type_url() -> Optional[str]:
    url = "https://pokeapi.co/api/v2/type/" #Url tipo agua
    data = fetch_data(url) #LLamamos al metodo anterior para obtener datos 

    if data is None: #If si no hay datos devolvemos none
        return None

    for poke_type in data.get('results', []): 
        if poke_type.get('name') == 'water':
            return poke_type.get('url')

    print("Water type not found.")
    return None

def fetch_water_pokemons() -> List[str]:
    water_url = get_water_type_url()

    if water_url is None:
        return []

    data = fetch_data(water_url)

    if data is None:
        return []

    
    pokemons = [pokemon['pokemon']['name'] for pokemon in data.get('pokemon', [])]
    
    return pokemons

def display_pokemons(pokemons: List[str]) -> None:
    if not pokemons:
        print("No Water-type Pokémon found.")
        return

    print("List of Water-type Pokémon:")
    for i, pokemon in enumerate(pokemons, 1):
        print(f"{i}. {pokemon}")
        
if __name__ == "__main__":
    water_pokemons = fetch_water_pokemons()
    display_pokemons(water_pokemons)
