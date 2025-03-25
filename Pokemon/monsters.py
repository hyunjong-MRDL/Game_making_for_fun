import attribute, nature

class Monster:
    monster_count = 0
    def __init__(self, name, attr, level, nature, BS, IV, EV, rank):
        # attr: Attribute (속성, 타입)
        # nature: 성격
        # BS: Base stats (종족값) -> LIST: [HP, PA, PD, SA, SD, SP])
        # IV: Individual values (개체값) -> LIST: [HP, PA, PD, SA, SD, SP])
        # EV: Effort values (노력치) -> LIST: [HP, PA, PD, SA, SD, SP])
        # rank: 랭크업 (이것도 종족값 별로 모두)
        self.name, self.attr, self.level, self.nature, self.BS, self.IV, self.EV, self.rank = name, attr, level, nature, BS, IV, EV, rank
        Monster.monster_count += 1
    
    # 경험치 계산 (현재 경험치 + 전투에서 획득한 경험치 -> 임계값 초과하면 레벨업) -> 이건 나중에...
    def __level_up__(self, curr_exp, acquired_exp):
        return
    
    def __net_ability__(self, stat_type):
        if stat_type == 0: # HP
            return int( ((2 * self.BS[stat_type] + self.IV[stat_type] + 0.25 * self.EV[stat_type] + 100) * 0.01 * self.level) + 10 )
        else:
            nature_effects = nature.__nature_effect_list__(self.nature)
            return int( ((2 * self.BS[stat_type] + self.IV[stat_type] + 0.25 * self.EV[stat_type]) * 0.01 * self.level + 5) * nature_effects[stat_type-1] )
    
class Battle:
    def __init__(self, monster1, monster2, weather):
        self.monster1, self.monster2 = monster1, monster2
    
    def __speed_decision__(self):
        monster1, monster2 = self.monster1, self.monster2
        spd1, spd2 = monster1.__net_ability__("SP"), monster2.__net_ability__("SP")