from Pokemon import Pokemon
from PokemonList import PokemonList

pokemons = PokemonList('./data/pokemon.csv')
print(pokemons.pokemons[0])