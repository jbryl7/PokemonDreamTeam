from Pokemon import Pokemon
from PokemonList import PokemonList
from solver import *
from PokemonTeam import PokemonTeam

import pandas as pd

path_to_data = './data/pokemon.csv'
pokemons = PokemonList().from_file(path_to_data)
poks = copy(pokemons)
# uncomment if ties aren't equal to bonus points
# pokemons.fight_results[pokemons.fight_results == .5] = 0 

s = Solver(pokemons)
print('grredy')
t0 = s.solve_greedy()
print(t0)
print(goal_fun_unique_defeated_pokemons(t0))
print('avg')
t1 = s.solve_random_search(150, goal_fun=goal_fun_team_sum_score)
print(t1)
print('abs')
t2 = s.solve_random_search(150, goal_fun=goal_fun_unique_defeated_pokemons)
print(t2)
print('median')
t3 = s.solve_random_search(150, goal_fun=goal_fun_team_median_score)
print(t3)


t0.simulate_fight(t1)
t0.simulate_fight(t2)
t0.simulate_fight(t3)

# t1.simulate_fight(t2)
# t1.simulate_fight(t3)
# t2.simulate_fight(t3)

# t2.simulate_fight(t3)
# t4 = t2.random_neighbor().random_neighbor().random_neighbor().random_neighbor()
# print('t4 i t2')
# t2.simulate_fight(t4)
# t5 = t4.random_neighbor().random_neighbor().random_neighbor()
# t4.simulate_fight(t5)


