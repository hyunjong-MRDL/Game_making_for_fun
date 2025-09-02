import random

class Battle:
    def __init__(self, my_monster, opponent):
        pass

    @staticmethod
    def _speed_decision(monster1, monster2):
        spd1, spd2 = monster1.__net_ability__(4), monster2.__net_ability__(4)
        if spd1 > spd2:
            return monster1
        elif spd2 > spd1:
            print(f"{monster2.name} first.")
            return monster2
        else: # SAME speed
            while True:
                token1, token2 = random.random(), random.random()
                if token1 != token2: break
            if token1 > token2:
                return monster1
            else:
                return monster2
    
    @staticmethod
    def calculate_exp(winner, loser, is_trainer_battle, num_participants=1, has_lucky_egg=False, is_traded=False):
        a = 1.5 if is_trainer_battle else 1.0
        
        base_exp = loser.base_exp # monsters.py와 encyclopedia.py에 추가 필요

        gained_exp = (a * base_exp * loser.level) / 7
        
        if is_traded:
            gained_exp *= 1.5
        if has_lucky_egg:
            gained_exp *= 1.5

        gained_exp /= num_participants
        
        return int(gained_exp)

class Trainer_Battle(Battle):
    def __init__(self, player1, player2):
        self.player1, self.player2 = player1, player2
    
    def get_first_attacker(self, monster1, monster2):
        return self._speed_decision(monster1, monster2)
    
    def __battle_EXP__(self, monster_win, monster_lose, num_participants=1):
        return self.calculate_exp(monster_win, monster_lose, is_trainer_battle=True, num_participants=num_participants)

class Wild_Battle(Battle):
    def __init__(self, monster1, monster2):
        self.monster1, self.monster2 = monster1, monster2
    
    def get_first_attacker(self, monster1, monster2):
        return self._speed_decision(monster1, monster2)
        
    def __battle_EXP__(self, monster_win, monster_lose, num_participants=1):
        return self.calculate_exp(monster_win, monster_lose, is_trainer_battle=False, num_participants=num_participants)