"""
Advent of Code 2023, Day 9
solution by Maja Sellmer
"""

with open('advent9.txt') as oasis_text:

    # PREPARE INPUT
    oasis_report = oasis_text.readlines()
    for i, line in enumerate(oasis_report):
        oasis_report[i] = [int(n) for n in line.rstrip('\n').split()]

    # PART 1 + 2
    predictions_sum = 0
    for history in oasis_report:
        current_diffs = history
        diffs_list = [history]
        # generate lists of step differences until fully zeros
        while any(current_diffs):
            next_diffs = [current_diffs[i+1]-current_diffs[i] for i in range(len(current_diffs)-1)]
            diffs_list.append(next_diffs)
            current_diffs = next_diffs
        # go back through the list and generate prediction at end/beginning
        diffs_list[-1].append(0)
        for j in range(2,len(diffs_list)+1):
            # diffs_list[-j].append(diffs_list[-j][-1]+diffs_list[-j+1][-1])
            diffs_list[-j].insert(0, diffs_list[-j][0]-diffs_list[-j+1][0])
        # predictions_sum += diffs_list[0][-1]
        predictions_sum += diffs_list[0][0]
    print(predictions_sum)
