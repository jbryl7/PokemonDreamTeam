import numpy as np
import pandas as pd
from Pokemon import Pokemon

class PokemonList:
    def __init__(self, pokemon_list = None, path_to_data= None):
        if (path_to_data is None):
            self.pokemons = pokemon_list
        else:
            df_pokemon = pd.read_csv(path_to_data)
            df_pokemon.set_index('pokedex_number', inplace=True)
            df_pokemon['type2'].fillna(value='nan', method = None, inplace=True)
            self.clean_capture_rate(df_pokemon)
            self.normalize(df_pokemon)
            self.pokemons = list()
            for i in range(1, 802):
                self.pokemons.append(Pokemon(df_pokemon.loc[i], i))
        self.fight_results = np.empty((len(self.pokemons) + 1, len(self.pokemons) + 1))
        self.initialize_fight_results()
        self.sum_of_fight_results = np.sum(self.fight_results, where=self.fight_results > 0.5, axis=1)
        

    def initialize_fight_results(self):
        for i in range(len(self.pokemons)):
            for j in range(i, len(self.pokemons)):
                res = self.pokemons[i].fight_result(self.pokemons[j])
                self.fight_results[i][j] = res
                self.fight_results[j][i] = abs(res - 1)
        self.fight_results.fill
    
    def clean_capture_rate(self, df):
        df.loc[df.capture_rate == '30 (Meteorite)255 (Core)', 'capture_rate'] = 35
        df['capture_rate'] = df.capture_rate.astype('int')

    def normalize(self, df):
        columns_to_update = ['capture_rate', 'base_happiness']
        print(columns_to_update)
        for col in columns_to_update:
            if col == 'base_happiness':
                df[col].update((df[col] - df[col].min()) / (df[col].max() - df[col].min()) - 0.5)
            else:
                df[col].update((df[col] - df[col].min()) / (df[col].max() - df[col].min()))
