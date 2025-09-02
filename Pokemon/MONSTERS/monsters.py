from . import attribute, nature
import random

class Monster:
    monster_count = 0
    def __init__(self, name, attr, level, nature, BS, IV, EV, level_type, EXP, base_exp):
        # attr: Attribute (속성, 타입)
        # nature: 성격
        # BS: Base stats (종족값) -> LIST: [HP, PA, PD, SA, SD, SP])
        # IV: Individual values (개체값) -> LIST: [HP, PA, PD, SA, SD, SP])
        # EV: Effort values (노력치) -> LIST: [HP, PA, PD, SA, SD, SP])
        self.name = name
        self.attr, self.level, self.nature = attr, level, nature
        self.BS, self.IV, self.EV = BS, IV, EV
        self.level_type, self.EXP, self.base_exp = level_type, EXP, base_exp
        Monster.monster_count += 1
    
    # 경험치 계산 (현재 경험치 + 전투에서 획득한 경험치 -> 임계값 초과하면 레벨업)
    def __level_up__(self, acquired_EXP):
        level = self.level
        # 불규칙 그룹
        if self.level_type == "NONREGULAR":
            if level < 50:
                EXP_to_level_up = int(level ** 3 * (100 - level) / 50)
            elif (self.level >= 50) and (self.level < 68):
                EXP_to_level_up = int(level ** 3 * (150 - level) / 100)
            elif (self.level >= 68) and (self.level < 98):
                EXP_to_level_up = int(level ** 3 * ((1911 - 10 *level) / 3) / 500)
            elif (self.level >= 98) and (self.level < 100):
                EXP_to_level_up = int(level ** 3 * (160 - level) / 100)
        
        # 빠름 그룹
        elif self.level_type == "FAST":
            EXP_to_level_up = int(4 * level ** 3 / 5)
        
        # 중간 빠름 그룹
        elif self.level_type == "MEDIATE_FAST":
            EXP_to_level_up = int(level ** 3)
        
        # 중간 느림 그룹
        elif self.level_type == "MEDIATE_SLOW":
            EXP_to_level_up = int((6/5) * level ** 3 - 15 * level ** 2 + 100 * level - 140)
        
        # 느림 그룹
        elif self.level_type == "SLOW":
            EXP_to_level_up = int((5/4) * level ** 3)
        
        # 변동 그룹
        elif self.level_type == "VARYING":
            if self.level < 15:
                EXP_to_level_up = int(level ** 3 * ((level + 1) / 3 + 24) / 50)
            elif (self.level >= 15) and (self.level < 36):
                EXP_to_level_up = int(level ** 3 * (level + 14) / 50)
            elif (self.level >= 68) and (self.level < 98):
                EXP_to_level_up = int(level ** 3 * (level / 2 + 32) / 50)

        while acquired_EXP > 0:
            if ( (self.EXP + acquired_EXP) >= EXP_to_level_up):
                self.level += 1
                acquired_EXP -= EXP_to_level_up
            else:
                self.EXP += acquired_EXP
                acquired_EXP = 0
                break

        return
    
    def __net_ability__(self, stat_type):
        if stat_type == 0: # HP
            return int( ((2 * self.BS[stat_type] + self.IV[stat_type] + 0.25 * self.EV[stat_type] + 100) * 0.01 * self.level) + 10 )
        else:
            nature_effects = nature.__nature_effect_list__(self.nature)
            return int( ((2 * self.BS[stat_type] + self.IV[stat_type] + 0.25 * self.EV[stat_type]) * 0.01 * self.level + 5) * nature_effects[stat_type-1] )