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
        self.speed = int(row[34])
        self.is_legendary = int(row[39])


    # legends_multiplier - parametr został dostosowany w taki sposób aby pokemony legendarne 
    # występowały w około 10% drużyn generowanych przez algorytm losowy
    def hits_needed_to_be_defeated2(self, other_pokemon):
        k_attacks = 5
        hits_needed = self.health / self.hit_dmg2(other_pokemon) #- other_pokemon.happines * k_attacks
        if self.is_legendary:
            hits_needed *= 0.25
        print(other_pokemon.name, 'needs ' , hits_needed, ' to defeat', self.name)
        return hits_needed #+  10 * self.capture_rate

    def hits_needed_to_be_defeated(self, other_pokemon):
        k_attacks = 5
        hits_needed = self.health / self.hit_dmg(other_pokemon) - other_pokemon.happines * k_attacks
        if self.is_legendary:
            hits_needed *= 0.25

        return hits_needed +  5 * self.capture_rate

    def hit_dmg(self, other_pokemon):
        legend_multiplier = 1
        if other_pokemon.is_legendary == 1:
            legend_multiplier = 0.5
        return other_pokemon.attack * self.get_attack_multiplier(other_pokemon) / (self.defense) * legend_multiplier

    def hit_dmg2(self, other_pokemon):
        legend_multiplier = 1
        if other_pokemon.is_legendary == 1:
            legend_multiplier = 0.5
        return other_pokemon.attack * self.get_attack_multiplier2(other_pokemon) / (self.defense) * legend_multiplier

    def fight_result(self, other_pokemon):
        p1 = self.hits_needed_to_be_defeated(other_pokemon)
        p2 = other_pokemon.hits_needed_to_be_defeated(self)
         
        if p1 == p2:
            return 0.5
        elif p1 > p2: # p2 wins
            return 1
        # p1 wins
        return 0
    
    def get_attack_multiplier2(self, attacker):
        attacker_types = sorted(attacker.types, key=lambda k: self.against[k])
        if len(attacker_types) == 2:
            p1, p2 = 1.2,0.8
            return max(0.1, (self.against[attacker_types[0]] * p1 + self.against[attacker_types[1]] * p2)/2)
        multiplier = max(0.1, self.against[attacker_types[0]])
        print('multiplier', attacker.name,  ' against ', self.name, multiplier)
        return multiplier

    def get_attack_multiplier(self, attacker):
        attacker_types = sorted(attacker.types, key=lambda k: self.against[k])
        if len(attacker_types) == 2:
            p1, p2 = 1.2, 0.8
            return max(0.1, self.against[attacker_types[0]] * p1 + self.against[attacker_types[1]] * p2)
        multiplier = max(0.1, self.against[attacker_types[0]])
        return multiplier

    def __str__(self):
        return str(self.__dict__)