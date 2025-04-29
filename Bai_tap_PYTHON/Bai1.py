import requests
import csv

url = "https://pokeapi.co/api/v2/pokedex/12/"
response = requests.get(url)
data = response.json()

pokemon_list = []

for entry in data['pokemon_entries']:
    species_url = entry['pokemon_species']['url'].replace('pokemon-species', 'pokemon')
    pokemon_data = requests.get(species_url).json()

    info = {
        'number': pokemon_data['id'],
        'height': pokemon_data['height'],
        'weight': pokemon_data['weight'],
        'name': pokemon_data['name'],
        'type': ', '.join([t['type']['name'] for t in pokemon_data['types']]),
        'ThumbnailImage': pokemon_data['sprites']['front_default']
    }
    pokemon_list.append(info)

with open('Bai1_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['number', 'height', 'weight', 'name', 'type', 'ThumbnailImage'])
    writer.writeheader()
    writer.writerows(pokemon_list)

poison_pokemon = [p for p in pokemon_list if 'poison' in p['type'].lower()]
with open('Bai1_output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['number', 'height', 'weight', 'name', 'type', 'ThumbnailImage'])
    writer.writeheader()
    writer.writerows(poison_pokemon)


