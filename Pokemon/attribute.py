import numpy as np

type_list = ["Normal", "Fire", "Water", "Electric", "Leaf", "Ice", "Fight", "Poison", "Ground",
            "Fly", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fariy"]

raw_type_matrix = [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]

def update_type_matrix(type_effective_matrix):
    for i, row in enumerate(type_effective_matrix):
        attack_type = type_list[i]
        for j in range(len(row)):
            defend_type = type_list[j]

            # 0
            if attack_type == "Normal":
                if (defend_type == "Rock") or (defend_type == "Steel"): type_effective_matrix[i][j] = 0.5
                elif defend_type == "Ghost": type_effective_matrix[i][j] = 0.0
            # 1
            if attack_type == "Fire":
                if defend_type in ("Leaf", "Ice", "Bug", "Steel"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Fire", "Water", "Rock", "Dragon"): type_effective_matrix[i][j] = 0.5
            # 2
            if attack_type == "Water":
                if defend_type in ("Fire", "Ground", "Rock"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Water", "Leaf", "Dragon"): type_effective_matrix[i][j] = 0.5
            # 3
            if attack_type == "Electric":
                if defend_type in ("Water", "Fly"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Electric", "Leaf", "Dragon"): type_effective_matrix[i][j] = 0.5
                elif defend_type == "Ground": type_effective_matrix[i][j] = 0.0
            # 4
            if attack_type == "Leaf":
                if defend_type in ("Water", "Ground", "Rock"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Fire", "Leaf", "Poison", "Fly", "Bug", "Dragon", "Steel"): type_effective_matrix[i][j] = 0.5
            # 5
            if attack_type == "Ice":
                if defend_type in ("Leaf", "Ground", "Fly", "Dragon"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Fire", "Water", "Ice", "Steel"): type_effective_matrix[i][j] = 0.5
            # 6
            if attack_type == "Fight":
                if defend_type in ("Normal", "Ice", "Rock", "Dark", "Steel"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Poison", "Fly", "Psychic", "Bug", "Fairy"): type_effective_matrix[i][j] = 0.5
                elif defend_type == "Ghost": type_effective_matrix[i][j] = 0.0
            # 7
            if attack_type == "Poison":
                if defend_type in ("Leaf", "Fairy"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Poison", "Ground", "Rock", "Ghost"): type_effective_matrix[i][j] = 0.5
                elif defend_type == "Steel": type_effective_matrix[i][j] = 0.0
            # 8
            if attack_type == "Ground":
                if defend_type in ("Fire", "Electric", "Poison", "Rock", "Steel"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Leaf", "Bug"): type_effective_matrix[i][j] = 0.5
                elif defend_type == "Fly": type_effective_matrix[i][j] = 0.0
            # 9
            if attack_type == "Fly":
                if defend_type in ("Leaf", "Fight", "Bug"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Electric", "Rock", "Steel"): type_effective_matrix[i][j] = 0.5
            # 10
            if attack_type == "Psychic":
                if defend_type in ("Fight", "Poison"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Psychic", "Steel"): type_effective_matrix[i][j] = 0.5
                elif defend_type == "Dark": type_effective_matrix[i][j] = 0.0
            # 11
            if attack_type == "Bug":
                if defend_type in ("Leaf", "Psychic", "Dark"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Fire", "Fight", "Poison", "Fly", "Ghost", "Steel", "Fairy"): type_effective_matrix[i][j] = 0.5
            # 12
            if attack_type == "Rock":
                if defend_type in ("Fire", "Ice", "Fly", "Bug"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Fight", "Ground", "Steel"): type_effective_matrix[i][j] = 0.5
            # 13
            if attack_type == "Ghost":
                if defend_type in ("Psychic", "Ghost"): type_effective_matrix[i][j] = 1.5
                elif defend_type == "Dark": type_effective_matrix[i][j] = 0.5
                elif defend_type == "Normal": type_effective_matrix[i][j] = 0.0
            # 14
            if attack_type == "Dragon":
                if defend_type == "Dragon": type_effective_matrix[i][j] = 1.5
                elif defend_type == "Steel": type_effective_matrix[i][j] = 0.5
                elif defend_type == "Fairy": type_effective_matrix[i][j] = 0.0
            # 15
            if attack_type == "Dark":
                if defend_type in ("Psychic", "Ghost"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Fight", "Dark", "Fairy"): type_effective_matrix[i][j] = 0.5
            # 16
            if attack_type == "Steel":
                if defend_type in ("Ice", "Rock", "Fairy"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Fire", "Water", "Electric", "Steel"): type_effective_matrix[i][j] = 0.5
            # 17
            if attack_type == "Fairy":
                if defend_type in ("Fight", "Dragon", "Dark"): type_effective_matrix[i][j] = 1.5
                elif defend_type in ("Fire", "Poison", "Steel"): type_effective_matrix[i][j] = 0.5
    return type_effective_matrix

updated_type_matrix = update_type_matrix(raw_type_matrix)