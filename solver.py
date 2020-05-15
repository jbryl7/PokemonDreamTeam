from Pokemon import Pokemon
from PokemonTeam import PokemonTeam
from PokemonList import PokemonList
import numpy as np
from copy import copy

def goal_fun_team_sum_score(team):
    score = 0
    for i in team.pokemon_indexes:
        score += sum(team.pokemons.fight_results[i])
    return score

def goal_fun_team_median_score(team):
    scores = list()
    for i in team.pokemon_indexes:
        scores.append(team.pokemons.fight_results[i])
    return np.median(np.sum(scores, axis=1))
    
def goal_fun_unique_defeated_pokemons(team):
    score = 0
    scores = np.empty((6, len(team.pokemons)+1))
    abs_scores = np.empty((1, len(team.pokemons)+1))
    for i, index in enumerate(team.pokemon_indexes):
        scores[i] = team.pokemons.fight_results[index]
    abs_scores = np.amax(scores, axis=0)
    abs_score = np.sum(abs_scores)
    return abs_score


class Solver:
    def __init__(self, pokemons):
        self.pokemons = pokemons

    def solve_greedy(self):
        team = PokemonTeam(self.pokemons)
        pokemons_to_defeat = copy(self.pokemons)
        fight_results = copy(pokemons_to_defeat.fight_results)

        while len(team.pokemon_indexes) < 6:
            pok_index, pok_defeated = -1,-1
            for p_index in range(len(pokemons_to_defeat)):
                p_defeated = sum(pokemons_to_defeat.fight_results[p_index])
                if p_defeated > pok_defeated:
                    pok_index, pok_defeated = p_index, p_defeated
            team.add_pokemon(pok_index)
            pokemons_to_defeat = [pok for pok_index, pok in enumerate(pokemons_to_defeat) if pokemons_to_defeat.fight_results[p_index][pok_index] == 1]
            pokemons_to_defeat = PokemonList().from_list(pokemons_to_defeat)
            pokemons_to_defeat.initialize_fight_results()
        return team


    def solve_random_search(self, iters = 50, goal_fun = goal_fun_unique_defeated_pokemons):
        team = PokemonTeam(self.pokemons)
        team.add_pokemon(team.get_random_pokemon_index_that_is_not_in_team())
        for i in range(5):
            team.add_pokemon(team.get_random_pokemon_index_that_is_not_in_team())
        team_score = goal_fun(team)
        print(team_score)
        for i in range(iters):
            new_random_team = team.random_neighbor()
            new_random_team_score = goal_fun(new_random_team)
            if (team_score < new_random_team_score):
                print(team)
                team = new_random_team
                team_score = new_random_team_score
                print(new_random_team_score)
        return team
        


