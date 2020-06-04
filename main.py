from Pokemon import Pokemon
from PokemonList import PokemonList
from solver import *
from PokemonTeam import PokemonTeam
import numpy as np
import pandas as pd

path_to_data = './data/pokemon.csv'
pokemons = PokemonList().from_file(path_to_data)
poks = copy(pokemons)
# uncomment if ties aren't equal to bonus points
#pokemons.fight_results[pokemons.fight_results == .5] = 0 

s = Solver(pokemons)
t1 = s.solve_random_search(200)
t0 = s.solve_greedy()
