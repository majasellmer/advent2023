"""
Advent of Code 2023, Day 6
solution by Maja Sellmer
"""

with open('advent6.txt') as race_text:

    # PREPARE INPUT
    race = race_text.readlines()

    # PART 1
    times = [int(n) for n in race[0].lstrip('Time: ').rstrip('\n').split()]
    distances = [int(n) for n in race[1].lstrip('Distance: ').rstrip('\n').split()]
    possibilities_product = 1
    for n, time in enumerate(times):
        possibilities = 0
        record_distance = distances[n]
        for k in range(time):
            my_distance = (time-k)*k
            if my_distance > record_distance:
                possibilities += 1
        possibilities_product *= possibilities
    print(possibilities_product)

    # PART 2
    time = int(race[0].lstrip('Time: ').rstrip('\n').replace(' ', ''))
    record_distance = int(race[1].lstrip('Distance: ').rstrip('\n').replace(' ', ''))
    possibilities = 0
    for k in range(time):
        my_distance = (time-k)*k
        if my_distance > record_distance:
            possibilities += 1
    print(possibilities)
            