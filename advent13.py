"""
Advent of Code 2023, Day 11
solution by Maja Sellmer
"""

with open('advent13.txt') as patterns_text:

    # PREPARE INPUT
    # save each pattern as a list of strings representing the rows
    patterns_lines = patterns_text.readlines()
    patterns = []
    i = 0
    current_pattern = []
    for line in patterns_lines:
        if line == '\n':
            patterns.append(current_pattern)
            current_pattern = []
            continue
        current_pattern.append(line.rstrip('\n'))
    patterns.append(current_pattern)

    # PART 1
    # total_sum = 0
    # for pattern in patterns:
    #     # find horizontal line of symmetry
    #     last_row = pattern[0]
    #     found = False
    #     for i in range(1, len(pattern)):
    #         symmetry = False
    #         this_row = pattern[i]
    #         if this_row == last_row:
    #             symmetry = True
    #             for k in range(1, min(i, len(pattern)-i)):
    #                 if pattern[i-k-1] != pattern[i+k]:
    #                     symmetry = False
    #                     break
    #             if symmetry:
    #                 found = True
    #                 total_sum += 100*i
    #                 break
    #         last_row = this_row
    #     # if not found, find vertical line of symmetry
    #     if not found:
    #         pattern_columns = [str([row[j] for row in pattern]) for j in range(len(pattern[0]))]
    #         last_column = pattern_columns[0]
    #         for j in range(1, len(pattern[0])):
    #             symmetry = False
    #             this_column = pattern_columns[j]
    #             if this_column == last_column:
    #                 symmetry = True
    #                 for k in range(1, min(j, len(pattern[0])-j)):
    #                     if pattern_columns[j-k-1] != pattern_columns[j+k]:
    #                         symmetry = False
    #                         break
    #                 if symmetry:
    #                     total_sum += j
    #                     break
    #             last_column = this_column
    # print(total_sum)

    # PART 2
    def nearly_equal(string1, string2):
        """
        Function to check if the difference between two strings is at most one character.
        Input:  string1, string2 (two strings of equal length)
        Output: boolean
        """
        difference = False
        for n, char in enumerate(string1):
            if char != string2[n]:
                if difference:
                    return False
                difference = True
        return True

    total_sum = 0
    for pattern in patterns:
        # find horizontal line of symmetry
        last_row = pattern[0]
        found = False
        for i in range(1, len(pattern)):
            symmetry = False
            this_row = pattern[i]
            if this_row == last_row:
                symmetry = True
                diff = False
            elif nearly_equal(this_row, last_row):
                symmetry = True
                diff = True
            if symmetry:
                for k in range(1, min(i, len(pattern)-i)):
                    if pattern[i-k-1] != pattern[i+k]:
                        if nearly_equal(pattern[i-k-1], pattern[i+k]) and not diff:
                            diff = True
                            continue
                        symmetry = False
                        break
                if symmetry and diff:
                    found = True
                    total_sum += 100*i
                    break
            last_row = this_row
        # if not found, find vertical line of symmetry
        if not found:
            pattern_cols = [str([row[j] for row in pattern]) for j in range(len(pattern[0]))]
            last_column = pattern_cols[0]
            for j in range(1, len(pattern[0])):
                symmetry = False
                this_column = pattern_cols[j]
                if this_column == last_column:
                    symmetry = True
                    diff = False
                elif nearly_equal(this_column, last_column):
                    symmetry = True
                    diff = True
                if symmetry:
                    for k in range(1, min(j, len(pattern_cols)-j)):
                        if pattern_cols[j-k-1] != pattern_cols[j+k]:
                            if nearly_equal(pattern_cols[j-k-1], pattern_cols[j+k]) and not diff:
                                diff = True
                                continue
                            symmetry = False
                            break
                    if symmetry and diff:
                        total_sum += j
                        break
                last_column = this_column
    print(total_sum)
            