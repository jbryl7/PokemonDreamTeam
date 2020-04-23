from Pokemon import Pokemon
from PokemonTeam import PokemonTeam
from PokemonList import PokemonList


class Solver:
    def __init__(self, pokemons):
        self.pokemons = pokemons

    def solve_greedy(self):
        team = PokemonTeam()
        pokemons_to_defeat = list(self.pokemons)
        while len(team.pokemons) < 6:
            poks = PokemonList(pokemons_to_defeat)
            p_index,p, p_defeated = -1,-1,-1
            for p_index in range(len(poks.pokemons)):
                poks_defeated = sum(poks.fight_results[p_index])
                if poks_defeated > p_defeated:
                    p_index, p, p_defeated = p_index, poks.pokemons[p_index], poks_defeated
            team.pokemons.append(p)
            pokemons_to_defeat = [pok for pok_index, pok in enumerate(poks.pokemons) if poks.fight_results[p_index][pok_index] == 1]
        for p in team.pokemons:
            print(p.name)
        return team

