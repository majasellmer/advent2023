"""
Advent of Code 2023, Day 4
solution by Maja Sellmer
"""

with open('advent4.txt') as scratchcards_text:

    # PREPARE INPUT
    # save each scratchcard as [list of winning numbers, list of numbers you have]
    scratchcards = scratchcards_text.readlines()
    scratchcards_list = []
    for card in scratchcards:
        card = card.rstrip('\n').split(':')[1]
        winning_numbers, numbers_you_have = card.split('|')
        winning_numbers = [int(num) for num in winning_numbers.split()]
        numbers_you_have = [int(num) for num in numbers_you_have.split()]
        scratchcards_list.append([winning_numbers, numbers_you_have])

    # PART 1
    # points_sum = 0
    # for card in scratchcards_list:
    #     num_winning = 0
    #     for winning_number in card[0]:
    #         if winning_number in card[1]:
    #             num_winning += 1
    #     points_sum += 2**(num_winning-1) if num_winning > 0 else 0
    # print(points_sum)

    # PART 2
    # you start out with one of each scratchcard
    num_cards = [1 for n in range(len(scratchcards_list))]
    for n, card in enumerate(scratchcards_list):
        # check how many of the numbers you have are winning
        num_winning = 0
        for winning_number in card[0]:
            if winning_number in card[1]:
                num_winning += 1
        # win copies of the next num_winning scratchcards
        for i in range(1, num_winning+1):
            num_cards[n+i] += num_cards[n]
    print(sum(num_cards))
    