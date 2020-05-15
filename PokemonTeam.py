from PokemonList import PokemonList 
from Pokemon import Pokemon 
import random
from copy import copy

class PokemonTeam:
    def __init__(self, pokemons = None, pokemon_indexes = None):
        self.pokemons = pokemons
        self.pokemon_indexes = pokemon_indexes
        if self.pokemon_indexes == None:
            self.pokemon_indexes = list()

    def add_pokemon(self, pokemon_index):
        self.pokemon_indexes.append(pokemon_index)

    def random_neighbor(self):
        index_to_replace = random.randint(0, len(self.pokemon_indexes)-1)
        new_pokemon = self.get_random_pokemon_index_that_is_not_in_team()
        new_pokemon_indexes = self.pokemon_indexes.copy()
        new_pokemon_indexes[index_to_replace] = new_pokemon
        return PokemonTeam(self.pokemons, new_pokemon_indexes)

    def get_random_pokemon_index_that_is_not_in_team(self):
        new_index = random.randint(0, len(self.pokemons)-1)
        while(new_index in self.pokemon_indexes):
            new_index = random.randint(0, len(self.pokemons)-1)
        return new_index

    def simulate_fight(self, other_team):
        other_pokemons = {copy(other_team.pokemons[index]): True for index in other_team.pokemon_indexes}
        my_pokemons = {copy(self.pokemons[index]): True for index in self.pokemon_indexes}
        
        print(list(map(lambda k: k.name, my_pokemons.keys())))
        print('vs')
        print(list(map(lambda k: k.name, other_pokemons.keys())))
        print('FIGHT!')
       
        i,j = 0,0
        while(i < len(my_pokemons.keys()) and j < len(other_pokemons.keys())):
            m_p = list(my_pokemons.keys())[i]
            o_p = list(other_pokemons.keys())[j]
            self.simulate_fight_pok_vs_pok(m_p, o_p, my_pokemons, other_pokemons)
            if not my_pokemons[m_p]:
                i+=1
            if not other_pokemons[o_p]:
                j+=1

        print('Winners:')
        if(True in my_pokemons.values()):
            print(list(map(lambda k: k.name, my_pokemons.keys())))
        if(True in other_pokemons.values()):
            print(list(map(lambda k: k.name, other_pokemons.keys())))
        print('\n')
        
        
    def simulate_fight_pok_vs_pok(self, pok1, pok2, my_poks, other_poks):
        res = pok1.fight_result(pok2)
        pok1_hits_needed = pok1.hits_needed_to_be_defeated(pok2)
        pok2_hits_needed = pok2.hits_needed_to_be_defeated(pok1)
        hit_diff = int(abs(pok1_hits_needed - pok2_hits_needed))
        # print(pok1)
        # print(pok2)
        # print(hit_diff)
        if res == 1:
            other_poks[pok2] = False
        elif res == 0:
            my_poks[pok1] = False
        else:
            my_poks[pok1] = False
            other_poks[pok2] = False
        min_hits = min(pok1_hits_needed, pok2_hits_needed)
        pok1.health = max(0, pok1.health - pok1.hit_dmg(pok2) * min_hits)
        pok2.health = max(0, pok2.health - pok2.hit_dmg(pok1) * min_hits)
        print((pok1.name, pok1.health, pok2.health, pok2.name))

    def __str__(self):
        return str(list(map(lambda k: self.pokemons[k].name, self.pokemon_indexes)))

