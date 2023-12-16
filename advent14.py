"""
Advent of Code 2023, Day 14
solution by Maja Sellmer
"""

import copy

with open('advent14.txt') as platform_text:

    # PREPARE INPUT
    platform = platform_text.readlines()
    for m, line in enumerate(platform):
        platform[m] = list(line.rstrip('\n'))
    num_rows = len(platform)
    num_cols = len(platform[0])

    # PART 1 + 2
    def tilt(position, direction):
        """
        Function to tilt the platform in a given direction.
        The rounded rocks (O) roll, the cube-shaped rocks (#) stay in place.
        Input:  position (list of lists of characters)
                direction (must be 'N', 'S', 'E' or 'W')
        Output: new_position (list of lists of characters)
        """
        new_position = position
        # tilting north -> round rocks shift up
        if direction == 'N':
            for j in range(num_cols):
                num_round = 0
                for i in range(1, num_rows+1):
                    if position[-i][j] == 'O':
                        num_round += 1
                        new_position[-i][j] = '.'
                    elif position[-i][j] == '#':
                        for k in range(i-num_round,i):
                            new_position[-k][j] = 'O'
                        num_round = 0
                for k in range(num_round):
                    new_position[k][j] = 'O'
        # tilting south -> round rocks shift down
        elif direction == 'S':
            for j in range(num_cols):
                num_round = 0
                for i in range(num_rows):
                    if position[i][j] == 'O':
                        num_round += 1
                        new_position[i][j] = '.'
                    elif position[i][j] == '#':
                        for k in range(i-num_round,i):
                            new_position[k][j] = 'O'
                        num_round = 0
                for k in range(1,num_round+1):
                    new_position[-k][j] = 'O'
        # tilting east -> round rocks shift right
        elif direction == 'E':
            for i in range(num_rows):
                num_round = 0
                for j in range(num_cols):
                    if position[i][j] == 'O':
                        num_round += 1
                        new_position[i][j] = '.'
                    elif position[i][j] == '#':
                        for k in range(j-num_round,j):
                            new_position[i][k] = 'O'
                        num_round = 0
                for k in range(1,num_round+1):
                    new_position[i][-k] = 'O'
        # tilting west -> round rocks shift left
        elif direction == 'W':
            for i in range(num_rows):
                num_round = 0
                for j in range(1, num_cols+1):
                    if platform[i][-j] == 'O':
                        num_round += 1
                        new_position[i][-j] = '.'
                    elif position[i][-j] == '#':
                        for k in range(j-num_round,j):
                            new_position[i][-k] = 'O'
                        num_round = 0
                for k in range(num_round):
                    new_position[i][k] = 'O'
        return new_position

    # PART 1
    # platform_final = tilt(platform, 'N')

    # PART 2
    # track already encountered positions in list
    platforms = [copy.deepcopy(platform)]
    # perform spin cycles (tilting north, west, south, east)
    for n in range(1000000000):
        platform = tilt(platform, 'N')
        platform = tilt(platform, 'W')
        platform = tilt(platform, 'S')
        platform = tilt(platform, 'E')
        # if a position is encountered which has been seen before
        # a cycle of platform positions has been found
        if platform in platforms:
            cycle_beginning = platforms.index(platform)
            cycle_length = n + 1 - cycle_beginning
            break
        platforms.append(copy.deepcopy(platform))
    # get the position after 1000000000 cycles
    r = (1000000000 - cycle_beginning) % cycle_length + cycle_beginning
    platform_final = platforms[r]

    # PART 1 + 2
    total_load = 0
    # load caused by a rounded rock is the number of rows to south edge
    for row in range(1, num_rows+1):
        for col in range(num_cols):
            if platform_final[-row][col] == 'O':
                total_load += row
    print(total_load)
