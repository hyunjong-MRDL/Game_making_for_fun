def point_block(points):
    blocks = 5 * ["#"]
    
    if (points <= 79) and (points >= 60):
        blocks[-1] = "-"
    elif (points <= 59) and (points >= 40):
        blocks[-2:] = 2 * ["-"]
    elif (points <= 39) and (points >= 20):
        blocks[-3:] = 3 * "-"
    elif (points <= 19) and (points > 0):
        blocks[-4:] = 4 * "-"
    elif points == 0: blocks = 5 * "-"

    return blocks

def display_points(player_1, player_2, block_1, block_2):
    status = ["0~19", "20~39", "40~59", "60~79", "80~99"]
    
    print(f"    {player_1}    {player_2}\n")
    print("====================\n")

    for i in range(4, -1, -1):
        print(f"{status[i]}\t{block_1[i]}\t{block_2[i]}\n")
    
    return