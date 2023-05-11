def players_num(): #plan to make visual with pysimpleGUI
    print("how many players: ")
    player_count_input = input()
    player_count_input = int(player_count_input)
    if player_count_input > 52:
        print(f'too many players. Need to be less than 52')
        exit
    print(f"entered players: {player_count_input}")
    return player_count_input