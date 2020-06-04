from Pokemon import Pokemon
from PokemonTeam import PokemonTeam
from PokemonList import PokemonList
import numpy as np
from copy import copy

OPTIMAL_SCORE = 801

def goal_fun_unique_defeated_pokemons(team):
    ret = 0
    for i in range(len(team.pokemons)):
        ret += is_pok_defeated_by_team(team, i)
    return ret

def is_pok_defeated_by_team(team, enemy_index: int):
    sum_score = [0] * 6
    for i, pokemon_index in enumerate(team.pokemon_indexes):
        sum_score[i] = team.pokemons.fight_results[pokemon_index, enemy_index]
    return max(sum_score) 


class Solver:
    def __init__(self, pokemons):
        self.pokemons = pokemons
        self.goal_fun = goal_fun_unique_defeated_pokemons


    def solve_greedy(self):
        sum_results_for_each_pok = np.sum(self.pokemons.fight_results, axis=1)
        best_indices = np.argsort(sum_results_for_each_pok)
        team = PokemonTeam(self.pokemons, best_indices[-6:].tolist())
        print(team)
        print(self.goal_fun(team))
        return team

    def get_weakest_index(self, team):
        scores = {}
        for i, p in enumerate(team.pokemon_indexes):
            scores[np.sum(team.pokemons.fight_results[p])] = i
        return scores[max(scores.keys())]

    def solve_random_search(self, iters = 50, team = None):
        if team is None:
            team = PokemonTeam(self.pokemons)

        team.add_pokemon(team.get_random_pokemon_index_that_is_not_in_team())
        for i in range(5):
            team.add_pokemon(team.get_random_pokemon_index_that_is_not_in_team())

        team_score = self.goal_fun(team)
        print("random search start")
        print(team)
        print(team_score)
        for i in range(iters):
            new_random_team = team.random_neighbor()
            new_random_team_score = self.goal_fun(new_random_team)
            if (team_score < new_random_team_score):
                team = new_random_team
                team_score = new_random_team_score
                if team_score == OPTIMAL_SCORE:
                    print(f"found optimal score in ", i, " iteration")
                    break
        print("random search finish")
        print(team)
        print(self.goal_fun(team))
        return team
        


