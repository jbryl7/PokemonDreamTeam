from Pokemon import Pokemon
from PokemonList import PokemonList
from solver import *
from PokemonTeam import PokemonTeam
import numpy as np
import pandas as pd

path_to_data = './data/pokemon.csv'
pokemons = PokemonList().from_file(path_to_data)
poks = copy(pokemons)

s = Solver(pokemons)
# legend = 0
# for i in range(100):
#     t1 = s.solve_random_search(200)
#     if t1.contains_legendary():
#         legend += 1
# print(legend)

s.solve_greedy()
print(s.solve_greedy_remaining_enemies().contains_legendary())