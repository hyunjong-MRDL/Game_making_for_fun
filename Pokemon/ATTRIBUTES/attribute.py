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

# raw_effective_matrix = np.ones((len(effectiveness), len(effectiveness)))

# def update_type_matrix(type_effective_matrix):
#     for i, attack_type in enumerate(effectiveness):
#         for j, defend_type in enumerate(effectiveness):
#             if attack_type in effectiveness:
#                 eff = effectiveness[attack_type]
#                 if "strong" in eff and defend_type in eff["strong"]:
#                     type_effective_matrix[i][j] = 1.5
#                 elif "weak" in eff and defend_type in eff["weak"]:
#                     type_effective_matrix[i][j] = 0.5
#                 elif "zero" in eff and defend_type in eff["zero"]:
#                     type_effective_matrix[i][j] = 0.0
#     return type_effective_matrix

# updated_effective_matrix = update_type_matrix(raw_effective_matrix)

effective_matrix = [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 1.0, 1.0, 0.5, 1.0],
                    [1.0, 0.5, 0.5, 1.0, 1.5, 1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 0.5, 1.0, 0.5, 1.0, 1.5, 1.0],
                    [1.0, 1.5, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.5, 1.0, 1.0, 1.0, 1.5, 1.0, 0.5, 1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.5, 0.5, 0.5, 1.0, 1.0, 1.0, 0.0, 1.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0],
                    [1.0, 0.5, 1.5, 1.0, 0.5, 1.0, 1.0, 0.5, 1.5, 0.5, 1.0, 0.5, 1.5, 1.0, 0.5, 1.0, 0.5, 1.0],
                    [1.0, 0.5, 0.5, 1.0, 1.5, 0.5, 1.0, 1.0, 1.5, 1.5, 1.0, 1.0, 1.0, 1.0, 1.5, 1.0, 0.5, 1.0],
                    [1.5, 1.0, 1.0, 1.0, 1.0, 1.5, 1.0, 0.5, 1.0, 0.5, 0.5, 0.5, 1.5, 0.0, 1.0, 1.5, 1.5, 0.5],
                    [1.0, 1.0, 1.0, 1.0, 1.5, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.0, 1.5],
                    [1.0, 1.5, 1.0, 1.5, 0.5, 1.0, 1.0, 1.5, 1.0, 0.0, 1.0, 0.5, 1.5, 1.0, 1.0, 1.0, 1.5, 1.0],
                    [1.0, 1.0, 1.0, 0.5, 1.5, 1.0, 1.5, 1.0, 1.0, 1.0, 1.0, 1.5, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0],
                    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 1.5, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.0, 0.5, 1.0],
                    [1.0, 0.5, 1.0, 1.0, 1.5, 1.0, 0.5, 0.5, 1.0, 0.5, 1.5, 1.0, 1.0, 0.5, 1.0, 1.5, 0.5, 0.5],
                    [1.0, 1.5, 1.0, 1.0, 1.0, 1.5, 0.5, 1.0, 0.5, 1.5, 1.0, 1.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0],
                    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 1.0, 1.0, 1.5, 1.0, 0.5, 1.0, 1.0],
                    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 1.0, 0.5, 0.0],
                    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.5, 1.0, 1.0, 1.5, 1.0, 0.5, 1.0, 0.5],
                    [1.0, 0.5, 0.5, 0.5, 1.0, 1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 1.0, 1.0, 1.0, 0.5, 1.5],
                    [1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 1.5, 0.5, 1.0]]

def calculate_damage(attacker, defender, skill):
    atk_type = skill.skill_type
    def_type = defender.attr
    attack_stat = attacker.__net_ability__(1)
    defense_stat = defender.__net_ability__(2)

    atk_idx = effectiveness.index(atk_type)
    def_idx = effectiveness.index(def_type)
    type_multiplier = effective_matrix[atk_idx][def_idx]

    damage = type_multiplier * (((2 * attacker.level / 5 + 2) * skill.power * attack_stat / defense_stat) / 50 + 2)

    return int(damage)