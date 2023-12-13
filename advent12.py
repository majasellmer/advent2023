"""
Advent of Code 2023, Day 12
solution by Maja Sellmer
"""

from functools import lru_cache

with open('advent12.txt') as condition_records_text:

    # PREPARE INPUT
    condition_records = condition_records_text.readlines()
    for m, row in enumerate(condition_records):
        record1, record2 = row.rstrip('\n').split()
        record2 = tuple(int(n) for n in record2.split(','))
        condition_records[m] = [record1, record2]

    # PART 2
    for m, row in enumerate(condition_records):
        record1, record2 = row
        record1 = record1+'?'+record1+'?'+record1+'?'+record1+'?'+record1
        record2 = record2+record2+record2+record2+record2
        condition_records[m] = [record1, record2]

    # PART 1 + 2

    @lru_cache(maxsize=None)
    def get_groups(pattern):
        """
        Function to determine sizes of contiguous groups of damaged springs.
        Input:  springs (string)
        Output: tuple
        """
        j = pattern.find('#')
        groups_list = []
        while j >= 0:
            k = 0
            while pattern[j+k] == '#':
                k += 1
                if j+k == len(pattern):
                    break
            groups_list.append(k)
            if j+k == len(pattern):
                break
            j = pattern.find('#', j+k)
        return tuple(groups_list)

    @lru_cache(maxsize=None)
    def possibilities(pattern, target_groups):
        """
        Recursive function to calculate number of possible arrangements
        of damaged and operational spring fitting the pattern.
        Input:  springs (string)
                target_groups (tuple)
        Output: int
        """
        # if pattern matches target groups exactly -> +1
        if get_groups(pattern) == target_groups:
            return 1
        # find last occurrence of ?
        i = pattern.rfind('?')
        # if no ? left -> backtrack
        if i < 0:
            return 0
        # if ? is the last character -> try both possibilities
        if i == len(pattern) - 1:
            p1 = possibilities(pattern[:i]+'.', target_groups)
            p2 = possibilities(pattern[:i]+'#', target_groups)
            return p1+p2
        # else, get sizes of end groups (those after ?)
        end_groups = get_groups(pattern[(i+1):])
        new_target_groups = list(target_groups)
        # if operational spring directly after ? -> cut off after ?
        if pattern[i+1] == '.':
            if len(end_groups) == 0:
                return possibilities(pattern[:(i+1)], tuple(new_target_groups))
            if end_groups == target_groups[-len(end_groups):]:
                new_target_groups = new_target_groups[:-len(end_groups)]
                return possibilities(pattern[:(i+1)], tuple(new_target_groups))
            # if end groups don't match target -> backtrack
            return 0
        # if damaged spring directly after ?
        if pattern[i+1] == '#':
            # if too many groups after ? -> backtrack
            if len(target_groups) < len(end_groups):
                return 0
            # if end groups match target -> ? must be operational
            if end_groups == target_groups[-len(end_groups):]:
                new_target_groups = new_target_groups[:-len(end_groups)]
                return possibilities(pattern[:i]+'.', tuple(new_target_groups))
            # if group after ? too short -> ? must be damaged
            if len(end_groups) == 1 and target_groups[-1] > end_groups[0]:
                new_target_groups[-1] -= end_groups[0]
                return possibilities(pattern[:i]+'#', tuple(new_target_groups))
            if end_groups[1:] == target_groups[(-len(end_groups)+1):]:
                if target_groups[-len(end_groups)] > end_groups[0]:
                    new_target_groups = new_target_groups[:(-len(end_groups)+1)]
                    new_target_groups[-1] -= end_groups[0]
                    return possibilities(pattern[:i]+'#', tuple(new_target_groups))
            # if group after ? too long -> backtrack
            return 0

    # PART 1
    arrangements_sum = 0
    possibilities_list = []
    for row in condition_records:
        springs, groups = row
        arrangements_sum += possibilities(springs, groups)
    print(arrangements_sum)
