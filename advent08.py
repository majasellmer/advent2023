"""
Advent of Code 2023, Day 8
solution by Maja Sellmer
"""

import numpy as np

with open('advent08.txt') as maps_text:

    # PREPARE INPUT
    maps = maps_text.readlines()
    instructions = maps[0].rstrip('\n')
    num_instructions = len(instructions)
    network = {}
    for line in maps[2:]:
        line = line.rstrip('\n').split('=')
        network[line[0].strip()] = line[1].lstrip(' (').rstrip(')').split(', ')

    # PART 1
    starting_nodes = ['AAA']

    # PART 2
    starting_nodes = []
    for node in list(network.keys()):
        if node[-1] == 'A':
            starting_nodes.append(node)

    # PART 1 + 2
    step_numbers = []
    instructions_counter = 0
    for starting_node in starting_nodes:
        current_node = starting_node
        instructions_counter = 0
        # while current_node != 'ZZZ':
        while current_node[-1] != 'Z':
            if instructions[instructions_counter % num_instructions] == 'L':
                current_node = network[current_node][0]
            else:
                current_node = network[current_node][1]
            instructions_counter += 1
        step_numbers.append(instructions_counter)
    print(step_numbers)
    print(np.lcm.reduce(step_numbers, dtype=np.int64))
