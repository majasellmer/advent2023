"""
Advent of Code 2023, Day 1
solution by Maja Sellmer
"""

with open('advent1.txt') as calibration_document:

    # PREPARE INPUT
    calibration_lines = calibration_document.readlines()
    for line in calibration_lines:
        line = line.rstrip('\n')
    digits_lists_list = []

    # PART 1
    # for line in calibration_lines:
    #     digits_list = []
    #     for char in line:
    #         if char.isdigit():
    #             digits_list.append(int(char))
    #     digits_lists_list.append(digits_list)

    # PART 2
    digits_spelled_out = ['one', 'two', 'three', 'four', 'five',
                          'six', 'seven', 'eight', 'nine']
    for line in calibration_lines:
        # create list to record all the digits in
        digits_list = []
        # find indices for all appearances of spelled out digits in the line
        digits_indices = []
        digits_indices_merged = []
        for digit in digits_spelled_out:
            digit_indices = []
            if digit in line:
                digit_index = 0
                while digit in line[digit_index:]:
                    digit_index += line[digit_index:].find(digit)
                    digit_indices.append(digit_index)
                    digit_index += len(digit)
            digits_indices.append(digit_indices)
            digits_indices_merged += digit_indices
        # go through the line
        i = 0
        while i < len(line):
            # add spelled out digits to list
            if i in digits_indices_merged:
                n = 0
                while n < 9:
                    if i in digits_indices[n]:
                        digits_list.append(n+1)
                        i += len(digits_spelled_out[n])-2
                        break
                    n += 1
                continue
            # add numeric digits to list
            if line[i].isdigit():
                digits_list.append(int(line[i]))
            i += 1
        digits_lists_list.append(digits_list)

    # PART 1 + 2
    calibration_values_sum = 0
    for digits_list in digits_lists_list:
        # the calibration value consists of the first and last digit
        calibration_value = 10*digits_list[0] + digits_list[-1]
        calibration_values_sum += calibration_value
    print(calibration_values_sum)
