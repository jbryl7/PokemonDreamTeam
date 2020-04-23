class PokemonTeam:
    def __init__(self, pokemons = None):
        if pokemons:
            self.pokemons = pokemons
        else:
            self.pokemons = list()

    def fight(self, other_team):
        other_pokemons = {pokemon: True for pokemon in other_team.pokemons}
        my_pokemons = {pokemon: True for pokemon in self.pokemons}
        my_poks_keys = my_pokemons.keys()
        i,j = 0,0
        while(i < len(my_poks_keys) and j < len(my_poks_keys)):
            m_p = list(my_pokemons.keys())[i]
            o_p = list(other_pokemons.keys())[j]
            self.fight_pok_vs_pok(m_p, o_p, my_pokemons, other_pokemons)
            if not my_pokemons[m_p]:
                i+=1
            if not other_pokemons[o_p]:
                j+=1

        print(True in my_pokemons.values())
        print(True in other_pokemons.values())
    def fight_pok_vs_pok(self, pok1, pok2, my_poks, other_poks):
        res = pok1.fight_result(pok2)
        pok1_hits_needed = pok1.hits_needed_to_be_defeated(pok2)
        pok2_hits_needed = pok2.hits_needed_to_be_defeated(pok1)
        hit_diff = int(abs(pok1_hits_needed - pok2_hits_needed))
    
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
        return str(self.__dict__)
