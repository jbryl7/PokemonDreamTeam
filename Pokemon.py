import numpy as np
class Pokemon:
    def __init__(self, row, pokedex_number):
        self.name = row[30]
        self.pokedex_number = pokedex_number
        self.types = [row[35]]
        if row[36] != 'nan':
            self.types.append(row[36])
        self.against = {
            "bug": float(row[1]),
            "dark": float(row[2]),
            "dragon": float(row[3]),
            "electric": float(row[4]),
            "fairy": float(row[5]),
            "fighting": float(row[6]),
            "fire": float(row[7]),
            "flying": float(row[8]),
            "ghost": float(row[9]),
            "grass": float(row[10]),
            "ground": float(row[11]),
            "ice": float(row[12]),
            "normal": float(row[13]),
            "poison": float(row[14]),
            "psychic": float(row[15]),
            "rock": float(row[16]),
            "steel": float(row[17]),
            "water": float(row[18]),
        }
        self.attack = float(row[19])
        self.happines = float(row[21])
        self.base_total = float(row[22])
        self.capture_rate = float(row[23])
        self.defense = float(row[25])
        self.health = float(row[28])
        self.s_attack = int(row[32])
        self.s_defense = int(row[33])
        self.is_legendary = int(row[39])

    def hits_needed_to_be_defeated(self, other_pokemon):
        k_attacks = 5
        hits_needed = self.health / self.hit_dmg(other_pokemon) + other_pokemon.happines * k_attacks
        if self.is_legendary:
            hits_needed *= 0.3
        return hits_needed

    def hit_dmg(self, other_pokemon):
        return other_pokemon.attack / (self.defense * self.get_defense_multiplier(other_pokemon))

    def fight_result(self, other_pokemon):
        p1 = self.hits_needed_to_be_defeated(other_pokemon)
        p2 = other_pokemon.hits_needed_to_be_defeated(self)
         
        if p1 == p2:
            return 0.5
        elif p1 > p2: # p2 wins
            return 1
        else: # p1 wins
            return 0
    
    def get_defense_multiplier(self, attacker):
        attacker_types = sorted(attacker.types, key=lambda k: self.against[k])
        if len(attacker_types) == 2:
            p1, p2 = 0.35, 0.65
            return max(0.1, self.against[attacker_types[0]] * p1 + self.against[attacker_types[1]] * p2)
        else:
            return max(0.1, self.against[attacker_types[0]])

    def __str__(self):
        return str(self.__dict__)