"""
Advent of Code 2023, Day 11
solution by Maja Sellmer
"""

with open('advent11.txt') as universe_text:

    # PREPARE INPUT
    universe = universe_text.read().splitlines()

    # PART 1 + 2
    # for part 1, the expansion factor is 1
    expansion_factor = 999999
    # find galaxies
    galaxies = []
    galaxy_columns = []
    num_rows_inserted = 0
    for i, this_row in enumerate(universe):
        galaxy_index = this_row.find('#')
        # expand universe: empty rows
        if galaxy_index < 0:
            num_rows_inserted += expansion_factor
        while galaxy_index >= 0:
            galaxies.append([i + num_rows_inserted, galaxy_index])
            galaxy_columns.append(galaxy_index)
            galaxy_index = this_row.find('#', galaxy_index+1)
    # expand universe: empty columns
    num_cols_inserted = 0
    for j in range(len(universe[0])):
        if j not in galaxy_columns:
            for galaxy in galaxies:
                if galaxy[1] > j+num_cols_inserted:
                    galaxy[1] += expansion_factor
            num_cols_inserted += expansion_factor
    # sum distances between galaxies
    distances_sum = 0
    for n, galaxy1 in enumerate(galaxies):
        for galaxy2 in galaxies[(n+1):]:
            distances_sum += abs(galaxy1[0]-galaxy2[0])+abs(galaxy1[1]-galaxy2[1])
    print(distances_sum)
