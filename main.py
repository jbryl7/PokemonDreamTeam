from Pokemon import Pokemon
from PokemonList import PokemonList
from solver import Solver
from PokemonTeam import PokemonTeam
pokemons = PokemonList(None, './data/pokemon.csv')
p1 = pokemons.pokemons[0]
p2 = pokemons.pokemons[3]
p3 = pokemons.pokemons[6]

# t1 = Solver(pokemons.pokemons).solve_greedy()
t1 = PokemonTeam(pokemons.pokemons[0:12:2])
t2 = PokemonTeam(pokemons.pokemons[1:13:2])


t1.fight(t2)