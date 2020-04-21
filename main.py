from Pokemon import Pokemon
from PokemonList import PokemonList

pokemons = PokemonList(None, './data/pokemon.csv')
p1 = pokemons.pokemons[0]
p2 = pokemons.pokemons[3]
p3 = pokemons.pokemons[6]

print(p1)
print(p2)
print(p3)
print(p1.fight_result(p2))
print(p1.fight_result(p3))
print(pokemons.sum_of_fight_results)