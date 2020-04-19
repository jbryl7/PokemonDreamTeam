import numpy as np
import pandas as pd
from subprocess import check_output
from Pokemon import Pokemon
import itertools
print(check_output(["ls", "./data"]).decode("utf8"))

df_pokemon = pd.read_csv('./data/pokemon.csv')
print(df_pokemon.loc[0])

# print(df_pokemon.iloc[:])
df_pokemon.set_index('pokedex_number', inplace=True)

#todo normalize data
# capture_rate
#happiness

df_pokemon['type2'].fillna(value='nan', method = None, inplace=True)
pokemons = list()
for i in range(1, 802):
    pokemons.append(Pokemon(df_pokemon.loc[i], i))

print(pokemons[15])


def fight_results(pokemons):
    results = np.empty((len(pokemons), len(pokemons)))
    for i in range(len(pokemons)):
        for j in range(i, len(pokemons)):
            results[i] = pokemons[i].fight_result(pokemons[j])
    return results

print(fight_results(pokemons))