"""
Contains a class representing a pokedex. Holds all seen pokemon
and all known information about those pokemon.

Pulls data from pokeapi.co
"""
import requests
import json
from pprint import pprint


class Pokedex:
    def __init__(self):
        self.pokemon = {}

    def add_pokemon(self, pokemon_name):
        """Add a pokemon to the pokedex by name."""
        # Query the API for that pokemon info
        response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon_name)

        # Break if pokemon not found in API
        if not response:
            print(f"Sorry! {pokemon_name} doesnt exist in the database!")
            return

        # Unpack json response
        data = response.json()

        # Unpack name and type
        poke_type = data["types"][0]["type"]["name"]
        name = data["name"]

        # Create spot in pokedex if it doesn't exist
        if not poke_type in self.pokemon:
            self.pokemon[poke_type] = {name: {}}
        elif not name in self.pokemon[poke_type]:
            self.pokemon[poke_type].update({name: {}})
        else:
            print("You already logged that pokemon!")

        # Gather a few moves
        all_moves = data["moves"]
        moves = []
        i = 0
        while i < 2 and i < len(all_moves):
            moves.append(all_moves[i]["move"]["name"])
            i += 1

        # Put moves in pokedex
        self.pokemon[poke_type][name]["moves"] = moves

        # Add pokemon's id
        poke_id = data["id"]
        self.pokemon[poke_type][name]["id"] = poke_id

        # Add pokemon's weight and height
        weight = data["weight"]
        height = data["height"]
        self.pokemon[poke_type][name]["weight"] = weight
        self.pokemon[poke_type][name]["height"] = height

    def search(self, pokemon_name):
        """Returns true if pokemon is in the pokedex."""
        for poke_type in self.pokemon:
            if pokemon_name in self.pokemon[poke_type].keys():
                return True
        return False

    def print_names(self):
        """Prints all of the names of pokemon in the pokedex."""
        print()
        print("You Have the Following Pokemon")
        print("-" * 30)
        for poke_type in self.pokemon:
            for name in self.pokemon[poke_type].keys():
                print(name.title())
        print()
    
    def dump_pokedex(self):
        """Prints all info currently in pokedex."""
        pprint(self.pokemon)
