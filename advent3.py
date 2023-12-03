"""
Advent of Code 2023, Day 3
solution by Maja Sellmer
"""

with open('advent3.txt') as engine_schematic:

    # PREPARE INPUT
    engine_schematic_lines = engine_schematic.readlines()
    # get coordinates of all symbols
    symbols_coordinates = []
    for i, line in enumerate(engine_schematic_lines):
        line = line.rstrip('\n')
        for j, char in enumerate(line):
            if not char.isdigit() and char != '.':
                symbols_coordinates.append([i,j])
    part_numbers_lists_list = []

    # PART 1 + 2
    def is_adjacent_to_symbol(end_coords, length):
        """
        Function to check if a number is a part number (that is, it is adjacent
        to at least one symbol horizontally, vertically or diagonally).
        Input:  coordinates of next non-digit after number (list of two ints)
                length of the number (int)
        Output: boolean
        """
        row, col = end_coords
        # symbol to the right of the number
        if [row, col] in symbols_coordinates:
            return True
        # symbol to the left of the number
        if [row, col-length-1] in symbols_coordinates:
            return True
        for k in range(length + 2):
            # symbol above the number
            if [row-1, col-k] in symbols_coordinates:
                return True
            # symbol below the number
            if [row+1, col-k] in symbols_coordinates:
                return True
        return False
    # find all numbers and check which one are part_numbers
    for i, line in enumerate(engine_schematic_lines):
        line = engine_schematic_lines[i]
        part_numbers_list = []
        j = 0
        current_number_list = []
        while j < len(line):
            char = line[j]
            if char.isdigit():
                current_number_list.append(int(char))
                j += 1
                continue
            # if a non-digit is encountered after positive number of digits
            if current_number_list != []:
                l = len(current_number_list)
                if is_adjacent_to_symbol([i,j],l):
                    part_number = 0
                    for m in range(l):
                        part_number *= 10
                        part_number += current_number_list[m]
                    part_numbers_list.append([part_number, j-l, l])
                current_number_list = []
            j += 1
        part_numbers_lists_list.append(part_numbers_list)

    # PART 1
    # part_numbers_sum = 0
    # for part_numbers_list in part_numbers_lists_list:
    #     for part_number in part_numbers_list:
    #         part_numbers_sum += part_number[0]
    # print(part_numbers_sum)

    # PART 2
    gear_ratios_sum = 0
    # go through all symbols and check which ones are gears
    for symbol in symbols_coordinates:
        i, j = symbol
        adjacent_numbers = []
        for line in [i-1, i, i+1]:
            for part_number in part_numbers_lists_list[line]:
                if j in range(part_number[1]-1, part_number[1]+part_number[2]+1):
                    adjacent_numbers.append(part_number[0])
                    continue
        # a symbol is a gear if adjacent to exactly two part numbers
        # the gear ratio is their product
        if len(adjacent_numbers) == 2:
            gear_ratio = adjacent_numbers[0]*adjacent_numbers[1]
            gear_ratios_sum += gear_ratio
    print(gear_ratios_sum)
    