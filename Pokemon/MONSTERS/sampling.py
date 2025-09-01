from . import encyclopedia, monsters, nature
import random

def dict_key_sample():
    total_keys = list(encyclopedia.kanto_encyclopedia.keys())
    return random.choice(total_keys)

def nature_sample():
    nature_idx = random.randint(0, len(nature.nature_list)-1)
    return nature.nature_list[nature_idx]

def IV_sample():
    IV_range = list(range(32))
    return[random.choice(IV_range), random.choice(IV_range), random.choice(IV_range),
           random.choice(IV_range), random.choice(IV_range), random.choice(IV_range)]

def EV_init():
    return [0] * 6

def monster_sample():
    sample_dict = encyclopedia.kanto_encyclopedia[dict_key_sample()]
    sample_name = sample_dict["name"]
    sample_attribute = sample_dict["attribute"]
    sample_level = 1 # 야생의 경우는 sampling 구현
    sample_nature = nature_sample()
    sample_BS = sample_dict["BS"]
    sample_IV = IV_sample()
    sample_EV = EV_init()
    sample_lvl_type = sample_dict["EXP_group"]
    sample_EXP = 0
    return monsters.Monster(sample_name, sample_attribute, sample_level, sample_nature, sample_BS, sample_IV, sample_EV, sample_lvl_type, sample_EXP)