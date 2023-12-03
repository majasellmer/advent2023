"""
Advent of Code 2023, Day 2
solution by Maja Sellmer
"""

with open('advent2.txt') as games_text:

    # PREPARE INPUT
    # save each game as [ID, [round 1, round 2, ...]]
    # each round as [num red cubes, num green cubes, num blue cubes]
    games = games_text.readlines()
    games_list = []
    for game in games:
        game = game.rstrip('\n').split(':')
        game_id = int(game[0].split()[1])
        game_rounds = game[1].split(';')
        game_rounds_list = []
        for game_round in game_rounds:
            game_round = game_round.strip().split(',')
            red = 0
            green = 0
            blue = 0
            for colour in game_round:
                colour = colour.split()
                if colour[1] == 'red':
                    red = int(colour[0])
                elif colour[1] == 'green':
                    green = int(colour[0])
                else:
                    blue = int(colour[0])
            game_rounds_list.append([red, green, blue])
        games_list.append([game_id, game_rounds_list])

    # PART 1
    # possible_games_sum = 0
    # for game in games_list:
    #     game_id, game_rounds_list = game
    #     game_possible = True
    #     for game_round in game_rounds_list:
    #         if game_round[0] > 12:
    #             game_possible = False
    #             break
    #         if game_round[1] > 13:
    #             game_possible = False
    #             break
    #         if game_round[2] > 14:
    #             game_possible = False
    #             break
    #     if game_possible:
    #         possible_games_sum += game_id
    # print(possible_games_sum)

    # PART 2
    power_sum = 0
    for game in games_list:
        game_id, game_rounds_list = game
        # find smallest necessary number of cubes of each colour
        max_red = 0
        max_green = 0
        max_blue = 0
        for game_round in game_rounds_list:
            if game_round[0] > max_red:
                max_red = game_round[0]
            if game_round[1] > max_green:
                max_green = game_round[1]
            if game_round[2] > max_blue:
                max_blue = game_round[2]
        # power of a set of cubes is the product of the three numbers
        power_sum += max_red*max_green*max_blue
    print(power_sum)
        