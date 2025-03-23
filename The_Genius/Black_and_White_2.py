import utils, random, os

print("흑과 백 (II) 게임에 오신 것을 환영합니다!\n")

while True:
    game_start = input("게임을 시작하려면 O, 종료하려면 X, 룰 설명이 필요하면 H를 입력하십시오: ").strip().upper()

    if game_start not in ["O", "X", "H"]:
        print("잘못된 입력입니다. 다시 입력해 주십시오.\n")
        continue

    # 게임 룰 설명
    if game_start == "H":
        print("게임 룰:")
        continue

    # 사용자 입력에 따른 게임 종료
    if game_start == "X":
        print("게임을 종료합니다.\n")
        break
    
    # 게임 시작
    print("게임을 시작합니다!\n\n")
    input("")
    os.system("cls")

    # 후공권 결정
    print("양 쪽 플레이어 모두 1~10 사이의 카드를 뽑습니다.\n")
    print("더 높은 카드를 뽑은 쪽이 후공권을 가집니다.\n")
    print("각 플레이어는 플레이어1, 플레이어2 중에 하나를 선택하십시오.\n")
    print()
    while True:
        input("선택이 완료되면 엔터 키를 눌러주십시오. ")
        card_A, card_B = random.randint(1, 10), random.randint(1, 10)
        print(f"플레이어1: {card_A}\n")
        print(f"플레이어2: {card_B}\n")
        if card_A == card_B:
            print("무승부 입니다. 양 쪽 플레이어는 카드를 다시 뽑습니다.\n")
            continue
        elif card_A > card_B:
            first_player, second_player = "플레이어2", "플레이어1"
            break
        else:
            first_player, second_player = "플레이어1", "플레이어2"
            break
    print(f"{first_player} (선공), {second_player} (후공)")
    first_points, second_points = 99, 99
    first_scores, second_scores = 0, 0
    input("")
    os.system("cls")

    # 총 9 라운드 진행
    for round in range(1, 10):
        # 선공 플레이어 턴
        first_block = utils.point_block(first_points)
        second_block = utils.point_block(second_points)
        utils.display_points(first_player, second_player, first_block, second_block)

        first_attack = int(input(f"({first_player}) 사용할 포인트를 입력해 주십시오: "))
        os.system("cls")

        first_points -= first_attack
        first_block = utils.point_block(first_points)
        utils.display_points(first_player, second_player, first_block, second_block)

        # 후공 플레이어 턴
        second_attack = int(input(f"({second_player}) 사용할 포인트를 입력해 주십시오: "))
        os.system("cls")

        second_points -= second_attack
        second_block = utils.point_block(second_points)
        utils.display_points(first_player, second_player, first_block, second_block)

        # 라운드 승패 확인
        if first_attack == second_attack:
            print("무승부입니다.\n")
            input("")
            os.system("cls")
            continue
        elif first_attack > second_attack:
            print(f"라운드{round} 결과: {first_player}가 이겼습니다, 1점을 획득합니다.\n")
            first_scores += 1
            print(f"{first_player}: {first_scores}점\t{second_player}: {second_scores}점.\n")
            input("")
            os.system("cls")
        else:
            print(f"라운드{round} 결과: {second_player}가 이겼습니다, 1점을 획득합니다.\n")
            second_scores += 1
            print(f"{first_player}: {first_scores}점\t{second_player}: {second_scores}점.\n")
            input("")
            os.system("cls")

        # 전체 라운드 조기 종료
        if (round < 9):
            if first_scores == 5: winner = first_player
            elif second_scores == 5: winner = second_player

    if first_scores == second_scores:
        print("최종 결과: 무승부 입니다. 양 쪽 플레이어 모두 수고하셨습니다.\n")
        input("")
        os.system("cls")
    elif first_scores > second_scores:
        print(f"최종 결과: {first_player}가 우승하였습니다. 축하드립니다.\n")
        input("")
        os.system("cls")
    elif first_scores < second_scores:
        print(f"최종 결과: {second_player}가 우승하였습니다. 축하드립니다.\n")
        input("")
        os.system("cls")