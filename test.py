"""Test Cases for Pokedex."""
from pokedex import Pokedex


my_pokemon = Pokedex()

pokemon_to_add = ["bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon",
                  "charizard", "squirtle", "wartortle", "blastoise", "caterpie",
                  "pikachu", "raichu", "poliwhirl", "vulpix", "ninetales",
                  "zubat", "diglett", "psyduck", "growlithe", "arcanine"]

for pokemon in pokemon_to_add:
    my_pokemon.add_pokemon(pokemon)

my_pokemon.dump_pokedex()
my_pokemon.print_names()

print(my_pokemon.search("raichu"))
print(my_pokemon.search("butterfree"))
