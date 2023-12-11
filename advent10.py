"""
Advent of Code 2023, Day 10
solution by Maja Sellmer
"""

with open('advent10.txt') as pipes_text:

    # PREPARE INPUT
    pipes = pipes_text.readlines()
    start_possibilities = ['|', '-', 'J', 'F', 'L', '7']
    # find starting coordinates and neighbours, replace S by fitting symbol
    for i, line in enumerate(pipes):
        j = line.find('S')
        if j >= 0:
            start_coords = [i, j]
            neighbour_coords = []
            if pipes[i][j-1] in ['-', 'L', 'F'] and pipes[i][j+1] in ['-', 'J', '7']:
                pipes[i] = line.replace('S', '-')
                x, y, direction = [i, j+1, 'R']
                end_coords = [i, j-1]
            elif pipes[i][j-1] in ['-', 'L', 'F'] and pipes[i-1][j] in ['|', '7', 'F']:
                pipes[i] = line.replace('S', 'J')
                x, y, direction = [i-1, j, 'U']
                end_coords = [i, j-1]
            elif pipes[i][j+1] in ['-', 'J', '7'] and pipes[i-1][j] in ['|', '7', 'F']:
                pipes[i] = line.replace('S', 'L')
                x, y, direction = [i-1, j, 'U']
                end_coords = [i, j+1]
            elif pipes[i][j+1] in ['-', 'J', '7'] and  pipes[i+1][j] in ['|', 'L', 'J']:
                pipes[i] = line.replace('S', 'F')
                x, y, direction = [i, j+1, 'R']
                end_coords = [i+1, j]
            elif pipes[i-1][j] in ['|', '7', 'F'] and pipes[i+1][j] in ['|', 'L', 'J']:
                pipes[i] = line.replace('S', '|')
                x, y, direction = [i-1, j, 'U']
                end_coords = [i+1, j]
            elif pipes[i][j-1] in ['-', 'L', 'F'] and pipes[i+1][j] in ['|', 'L', 'J']:
                pipes[i] = line.replace('S', '7')
                x, y, direction = [i+1, j, 'D']
                end_coords = [i, j-1]
            break
    x_max = len(pipes)
    y_max = len(pipes[0])-1

    # PART 1 + 2
    # follow the loop, record coordinates in list
    loop_coords = [start_coords, [x,y]]
    while [x, y] != end_coords:
        # | is a vertical pipe connecting north and south
        if pipes[x][y] == '|':
            x = x-1 if direction == 'U' else x+1
        # - is a horizontal pipe connecting east and west
        elif pipes[x][y] == '-':
            y = y-1 if direction == 'L' else y+1
        # L is a 90-degree bend connecting north and east
        elif pipes[x][y] == 'L':
            if direction == 'D':
                y += 1; direction = 'R'
            else:
                x -= 1; direction = 'U'
        # J is a 90-degree bend connecting north and west
        elif pipes[x][y] == 'J':
            if direction == 'D':
                y -= 1; direction = 'L'
            else:
                x -= 1; direction = 'U'
        # 7 is a 90-degree bend connecting south and west
        elif pipes[x][y] == '7':
            if direction == 'U':
                y -= 1; direction = 'L'
            else:
                x += 1; direction = 'D'
        # F is a 90-degree bend connecting south and east
        elif pipes[x][y] == 'F':
            if direction == 'U':
                y += 1; direction = 'R'
            else:
                x += 1; direction = 'D'
        loop_coords.append([x,y])

    # PART 1
    # distance to the point farthest from the origin is half the length of the loop
    print(len(loop_coords)/ 2)

    # PART 2
    # line by line, find all the points which are inside the loop
    inside_coords = []
    for x in range(x_max):
        loop_entered = False
        on_loop = False
        for y in range(y_max):
            if [x, y] in loop_coords:
                if on_loop:
                    if pipes[x][y] == '-':
                        continue
                    on_loop = False
                    if pipes[x][y] == '7':
                        loop_entered = not loop_entered
                else:
                    if pipes[x][y] == '|':
                        loop_entered = not loop_entered
                        continue
                    on_loop = True
                    if pipes[x][y] == 'F':
                        loop_entered = not loop_entered
                continue
            if loop_entered:
                inside_coords.append([x,y])
    print(len(inside_coords))
