from Pokemon import Pokemon
from PokemonList import PokemonList
from solver import Solver
import PokemonTeam
pokemons = PokemonList(None, './data/pokemon.csv')
p1 = pokemons.pokemons[0]
p2 = pokemons.pokemons[3]
p3 = pokemons.pokemons[6]

Solver(pokemons.pokemons).solve_greedy()