class PokemonTeam:
    def __init__(self, pokemons = None):
        if pokemons:
            self.pokemons = pokemons
        else:
            self.pokemons = list()

    def fight(self, other_team):
        other_pokemons = {pokemon: True for pokemon in other_team.pokemons}

    
    def __str__(self):
        return str(self.__dict__)
