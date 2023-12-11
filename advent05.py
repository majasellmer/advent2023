"""
Advent of Code 2023, Day 5
solution by Maja Sellmer
"""

with open('advent05.txt') as almanac_text:

    # PREPARE INPUT
    almanac = almanac_text.readlines()
    seeds = [int(n) for n in almanac[0].lstrip('seeds: ').split()]
    # save all the maps as a list
    # each map is a piecewise linear function, save it as a list of pieces
    # with each piece as [source_start, source_end, dest_start, dest_end, shift]
    conversion_maps = []
    current_map = []
    for line in almanac[2:]:
        if line == '\n':
            current_map.sort(key=lambda x: x[1])
            conversion_maps.append(current_map)
            current_map = []
            continue
        if not line[0].isdigit():
            continue
        current_map.append([int(n) for n in line.rstrip('\n').split()])
    current_map.sort(key=lambda x: x[1])
    conversion_maps.append(current_map)
    for conv_map in conversion_maps:
        for n, conv_range in enumerate(conv_map):
            conv_map[n] = [conv_range[1], conv_range[1] + conv_range[2],
                           conv_range[0], conv_range[0] + conv_range[2],
                           conv_range[0] - conv_range[1]]

    # PART 1
    # def convert(number, conversion_map):
    #     for conversion_range in conversion_map:
    #         source_start, source_end, dest_start, dest_end, shift = conversion_range
    #         if number in range(source_start, source_end):
    #             return number + shift
    #     return number
    # locations = []
    # for seed in seeds:
    #     for conversion_map in conversion_maps:
    #         seed = convert(seed, conversion_map)
    #     locations.append(seed)
    # print(min(locations))

    # PART 2
    def convert_intervals(old_intervals, conversion_map):
        """
        Function to convert a list of intervals of seeds to soil, soil to fertilizer etc.
        Input:  old_intervals_list (list of lists of two ints)
                conversion_map (list of lists of five ints)
        Output: list of lists of two ints
        """
        new_intervals = []
        i = 0
        while i < len(old_intervals):
            left, right = old_intervals[i]
            done = False
            # there are four options for each interval:
            # 1. both left and right endpoint are contained in the same range
            # 2. left endpoint contained in a range, right not in the same range
            # 3. left endpoint not in any range, right in some range
            # 4. neither left nor right endpoint in any range
            for conversion_range in conversion_map:
                source_start, source_end, dest_start, dest_end, shift = conversion_range
                if left in range(source_start, source_end):
                    if right in range(source_start, source_end):
                        new_intervals.append([left + shift, right + shift])
                        done = True
                        break
                    new_intervals.append([left + shift, dest_end])
                    old_intervals.append([source_end, right])
                    done = True
                    break
                if right in range(source_start, source_end):
                    new_intervals.append([left, source_start])
                    new_intervals.append([dest_start, right+shift])
                    done = True
                    break
            if not done:
                new_intervals.append([left, right])
            i += 1
        return new_intervals
    # determine the intervals of seed numbers
    seed_intervals = []
    j = 0
    while j < len(seeds):
        range_start = seeds[j]
        range_length = seeds[j+1]
        seed_intervals.append([range_start, range_start+range_length])
        j += 2
    # convert through all the maps to get the locations
    for conv_map in conversion_maps:
        seed_intervals = convert_intervals(seed_intervals, conv_map)
    # find the minimal location
    seed_intervals.sort(key=lambda x: x[0])
    print(seed_intervals[0][0])
