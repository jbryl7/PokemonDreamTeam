import numpy as np
import pandas as pd
from Pokemon import Pokemon

class PokemonList(list):    
    def __init__(self, *args, **kwargs):
        self.fight_results = np.empty(0)
        super().__init__(*args, **kwargs)

    def from_list(self, poks):
        for p in poks:
            self.append(p)
        return self

    def from_file(self, path_to_data= None):
        print(path_to_data)
        df_pokemon = pd.read_csv(path_to_data)
        df_pokemon.set_index('pokedex_number', inplace=True)
        df_pokemon['type2'].fillna(value='nan', method = None, inplace=True)
        self.clean_capture_rate(df_pokemon)
        self.normalize(df_pokemon)
        for i in range(1, 802):
            self.append(Pokemon(df_pokemon.loc[i], i))
        self.initialize_fight_results()
        return self

    def initialize_fight_results(self):
        self.fight_results = np.empty((len(self) + 1, len(self) + 1))
        for i in range(len(self)):
            for j in range(i, len(self)):
                res = self[i].fight_result(self[j])
                self.fight_results[i][j] = res
                self.fight_results[j][i] = abs(res - 1)
        self.fight_results.fill
    
    def clean_capture_rate(self, df):
        df.loc[df.capture_rate == '30 (Meteorite)255 (Core)', 'capture_rate'] = 35
        df['capture_rate'] = df.capture_rate.astype('int')

    def normalize(self, df):
        columns_to_update = ['capture_rate', 'base_happiness']
        for col in columns_to_update:
            if col == 'base_happiness':
                df[col].update((df[col] - df[col].min()) / (df[col].max() - df[col].min()) - 0.5)
            else:
                df[col].update((df[col] - df[col].min()) / (df[col].max() - df[col].min()))
