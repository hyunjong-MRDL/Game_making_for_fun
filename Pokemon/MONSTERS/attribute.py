import numpy as np

effectiveness = {
    "Normal": {"weak": ["Rock", "Steel"], "zero": ["Ghost"]},
    "Fire": {"strong": ["Leaf", "Ice", "Bug", "Steel"], "weak": ["Fire", "Water", "Rock", "Dragon"]},
    "Water": {"strong": ["Fire", "Ground", "Rock"], "weak": ["Water", "Leaf", "Dragon"]},
    "Electric": {"strong": ["Water", "Fly"], "weak": ["Electric", "Leaf", "Dragon"], "zero": ["Ground"]},
    "Leaf": {"strong": ["Water", "Ground", "Rock"], "weak": ["Fire", "Leaf", "Poison", "Fly", "Bug", "Dragon", "Steel"]},
    "Ice": {"strong": ["Leaf", "Ground", "Fly", "Dragon"], "weak": ["Fire", "Water", "Ice", "Steel"]},
    "Fight": {"strong": ["Normal", "Ice", "Rock", "Dark", "Steel"], "weak": ["Poison", "Fly", "Psychic", "Bug", "Fairy"], "zero": ["Ghost"]},
    "Poison": {"strong": ["Leaf", "Fairy"], "weak": ["Poison", "Ground", "Rock", "Ghost"], "zero": ["Steel"]},
    "Ground": {"strong": ["Fire", "Electric", "Poison", "Rock", "Steel"], "weak": ["Leaf", "Bug"], "zero": ["Fly"]},
    "Fly": {"strong": ["Leaf", "Fight", "Bug"], "weak": ["Electric", "Rock", "Steel"]},
    "Psychic": {"strong": ["Fight", "Poison"], "weak": ["Psychic", "Steel"], "zero": ["Dark"]},
    "Bug": {"strong": ["Leaf", "Psychic", "Dark"], "weak": ["Fire", "Fight", "Poison", "Fly", "Ghost", "Steel", "Fairy"]},
    "Rock": {"strong": ["Fire", "Ice", "Fly", "Bug"], "weak": ["Fight", "Ground", "Steel"]},
    "Ghost": {"strong": ["Psychic", "Ghost"], "weak": ["Dark"], "zero": ["Normal"]},
    "Dragon": {"strong": ["Dragon"], "weak": ["Steel"], "zero": ["Fairy"]},
    "Dark": {"strong": ["Psychic", "Ghost"], "weak": ["Fight", "Dark", "Fairy"]},
    "Steel": {"strong": ["Ice", "Rock", "Fairy"], "weak": ["Fire", "Water", "Electric", "Steel"]},
    "Fairy": {"strong": ["Fight", "Dragon", "Dark"], "weak": ["Fire", "Poison", "Steel"]}
}

def create_effective_matrix():
    """
    Dynamic production of type effective matrix
    """
    types = list(effectiveness.keys())
    num_types = len(types)

    effective_matrix = np.ones((num_types, num_types))
    for i, attack_type in enumerate(types):
        eff_info = effectiveness[attack_type]
        
        if "strong" in eff_info:
            for defend_type in eff_info["strong"]:
                j = types.index(defend_type)
                effective_matrix[i, j] = 1.5
        if "weak" in eff_info:
            for defend_type in eff_info["weak"]:
                j = types.index(defend_type)
                effective_matrix[i, j] = 0.5
        if "zero" in eff_info:
            for defend_type in eff_info["zero"]:
                j = types.index(defend_type)
                effective_matrix[i, j] = 0.0
                
    return effective_matrix

effective_matrix = create_effective_matrix()

def calculate_damage(attacker, defender, skill):
    types = list(effectiveness.keys())
    atk_type = skill.skill_type
    def_type = defender.attr

    try:
        atk_idx = types.index(atk_type)
        def_idx = types.index(def_type)
    except ValueError:
        print(f"Error: Unknown type '{atk_type}' or '{def_type}'.")
        return 0

    attack_stat = attacker.__net_ability__(1)
    defense_stat = defender.__net_ability__(2)

    type_multiplier = effective_matrix[atk_idx, def_idx]

    damage = type_multiplier * (((2 * attacker.level / 5 + 2) * skill.power * attack_stat / defense_stat) / 50 + 2)

    return int(damage)