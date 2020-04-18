class Pokemon:
    def __init__(self, np_row):
        print(np_row)
        self.name = np_row[30]
        self.pokedex_number = np_row[32]
        self.is_legendary = np_row[40]
        self.types = [np_row[36]]
        if np_row[37]:
            self.types.append(np_row[37])
        self.health = np_row[28]
        self.attack = np_row[19]
        self.defense = np_row[25]
        self.s_attack = np_row[33]
        self.s_defense = np_row[34]
        self.happines = np_row[21]
        self.base_total = np_row[22]
        self.capture_rate = np_row[23]
        self.against = {
            "bug": float(np_row[1]),
            "dark": float(np_row[2]),
            "dragon": float(np_row[3]),
            "electric": float(np_row[4]),
            "fairy": float(np_row[5]),
            "fighting": float(np_row[6]),
            "fire": float(np_row[7]),
            "flying": float(np_row[8]),
            "ghost": float(np_row[9]),
            "grass": float(np_row[10]),
            "ground": float(np_row[11]),
            "ice": float(np_row[12]),
            "normal": float(np_row[13]),
            "poison": float(np_row[14]),
            "psychic": float(np_row[15]),
            "rock": float(np_row[16]),
            "steel": float(np_row[17]),
            "water": float(np_row[18]),
        }
    def hits_needed_to_be_defeated(self, other_pokemon):
        k_attacks = 3
        return self.health / 
        (other_pokemon.attack * 
        self.get_defense_multiplier(other_pokemon) /
         (self.defense / 2.0)) + other_pokemon.happines * k_attacks

    def fight_result(self, other_pokemon):
        p1 = self.hits_needed_to_be_defeated(other_pokemon)
        p2 = self.hits_needed_to_be_defeated(self)
         
        if p1 == p2:
            return 0.5
        elif p1 > p2: # p2 wins
            return 0
        else: # p1 wins
            return 1 
    
    def get_defense_multiplier(self, attacker):
        attacker_types = sorted(attacker.types, key=lambda k: self.against[k])
        if len(attacker_types) == 2:
            p1, p2 = 0.35, 0.65
            return self.against[attacker_types[0]] * p1 + self.against[attacker_types[1]] * p2    
        else:
            return self.against[attacker_types[0]]