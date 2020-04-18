import numpy as np
import pandas as pd
from subprocess import check_output
from Pokemon import Pokemon

print(check_output(["ls", "./data"]).decode("utf8"))

df_pokemon = pd.read_csv('./data/pokemon.csv')

print(df_pokemon.shape)
pokemons = list(map(lambda row: Pokemon(row), list(df_pokemon.T.iteritems())))