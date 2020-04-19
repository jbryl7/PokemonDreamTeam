import numpy as np
import pandas as pd
from Pokemon import Pokemon

class PokemonList:
    def __init__(self, path_to_data):
        df_pokemon = pd.read_csv(path_to_data)
        df_pokemon.set_index('pokedex_number', inplace=True)
        df_pokemon['type2'].fillna(value='nan', method = None, inplace=True)
        self.pokemons = list()
        for i in range(1, 802):
            self.pokemons.append(Pokemon(df_pokemon.loc[i], i))
        self.fight_results = np.empty((len(self.pokemons), len(self.pokemons)))
        self.initialize_fight_results()


    def initialize_fight_results(self):
        for i in range(len(self.pokemons)):
            for j in range(i, len(self.pokemons)):
                self.fight_results[i] = self.pokemons[i].fight_result(self.pokemons[j])
    
    