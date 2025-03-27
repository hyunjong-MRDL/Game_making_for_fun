#                         "" TOTAL STATS include HP ""
#                           0     1     2     3     4
nature_dependent_stats = ["PA", "PD", "SA", "SD", "SP"]

nature_list = ["Hardy", "Lonely", "Adamant", "Naughty", "Brave",
               "Bold", "Docile", "Impish", "Lax", "Relaxed",
               "Modest", "Mild", "Bashful", "Rash", "Quiet",
               "Calm", "Gentle", "Careful", "Quirky", "Sassy",
               "Timid", "Hasty", "Jolly", "Naive", "Serious"]

def __nature_effect_list__(nature_of_monster):
    nature_index = nature_list.index(nature_of_monster)
    row, col = nature_index//5, nature_index%5
    if row == col:
        return [1.0] * len(nature_dependent_stats)
    else:
        nature_effects = [1.0] * len(nature_dependent_stats)
        nature_effects[row] = 1.1  # boosted stat
        nature_effects[col] = 0.9  # reduced stat
        return nature_effects