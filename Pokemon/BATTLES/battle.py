import random

class Battle:
    def __init__(self, my_monster, opponent):
        pass
class Trainer_Battle:
    def __init__(self, player1, player2):
        self.player1, self.player2 = player1, player2
    
    def __speed_decision__(self, monster1, monster2): # 선공권을 가진 포켓몬 반환
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

    def __battle_EXP__(self, monster_win, monster_lose):
        winner_level, loser_level = monster_win.level, monster_lose.level
        winner_EXP = monster_win.EXP
        EXP_group = monster_win.level_type
        # 교환 포켓몬이면 경험치 획득량 증가,
        # 행복의 알을 지닌 포켓몬이 전투 승리시 경험치 획득량 증가
        # -> 추후에 구현하기
        return (1.5 * loser_level) / (7 * participated_num)

class Wild_Battle:
    def __init__(self, monster1, monster2):
        self.monster1, self.monster2 = monster1, monster2
    
    def __speed_decision__(self, monster1, monster2): # 선공권을 가진 포켓몬 반환
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

    def __battle_EXP__(self, monster_win, monster_lose):
        winner_level, loser_level = monster_win.level, monster_lose.level
        winner_EXP = monster_win.EXP
        EXP_group = monster_win.level_type
        return loser_level / (7 * participated_num)