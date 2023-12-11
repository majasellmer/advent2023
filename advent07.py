"""
Advent of Code 2023, Day 7
solution by Maja Sellmer
"""

from functools import cmp_to_key

with open('advent07.txt') as game_text:

    # PREPARE INPUT
    game = game_text.readlines()
    hands = {}
    for line in game:
        hands[line.rstrip('\n').split()[0]] = int(line.rstrip('\n').split()[1])
    hands_ranked = list(hands.keys())

    # PART 1 + 2
    type_strength = {'five of a kind':7, 'four of a kind':6, 'full house':5,
                     'three of a kind':4, 'two pair':3, 'one pair':2, 'high card':1}

    def compare(hand1, hand2):
        """
        Function for sorting to compare the strength of two hands.
        Input:  hand1 (string)
                hand2 (string)
        Output: 1, 0 or -1

        """
        # hands are first compared by type
        if type_strength[types[hand1]] > type_strength[types[hand2]]:
            return 1
        if type_strength[types[hand1]] < type_strength[types[hand2]]:
            return -1
        # if they are the same type
        # they are then compared by card strength, starting with the first card
        for i in range(5):
            if card_strength[hand1[i]] > card_strength[hand2[i]]:
                return 1
            if card_strength[hand1[i]] < card_strength[hand2[i]]:
                return -1
        return 0

    def get_hand_type(hand, with_joker):
        """
        Function to determine the type of a hand.
        The 'J' can stand for 'Jack' (with_joker = False) or 'Joker' (with_joker = True).
        Input:  hand (string)
                with_joker (boolean)
        Output: hand type (string)

        """
        # find out how many different card labels are in the hand
        different_cards = set(hand)
        # if there is a joker, the possibilites are:
        if with_joker and 'J' in different_cards:
            # JJJJJ or JJJJA or JJJAA or JJAAA or JAAAA
            if len(different_cards) <= 2:
                return 'five of a kind'
            # JJJAB or JJAAB or JAAAB or JAABB
            if len(different_cards) == 3:
                if hand.count('J') >= 2:
                    return 'four of a kind'
                c1 = different_cards.pop()
                c1 = different_cards.pop() if c1 == 'J' else c1
                if hand.count(c1) == 2:
                    return 'full house'
                return 'four of a kind'
            # JJABC or JAABC
            if len(different_cards) == 4:
                return 'three of a kind'
            # JABCD
            if len(different_cards) == 5:
                return 'one pair'
        # if there are no jokers, the possibilities are:
        # AAAAA
        if len(different_cards) == 1:
            return 'five of a kind'
        # AAAAB or AAABB
        if len(different_cards) == 2:
            c1 = different_cards.pop()
            if hand.count(c1) == 1 or hand.count(c1) == 4:
                return 'four of a kind'
            return 'full house'
        # AAABC or AABBC
        if len(different_cards) == 3:
            c1 = different_cards.pop()
            c2 = different_cards.pop()
            if hand.count(c1) == 2 or hand.count(c2) == 2:
                return 'two pair'
            return 'three of a kind'
        # AABCD
        if len(different_cards) == 4:
            return 'one pair'
        # ABCDE
        return 'high card'

    # PART 1
    # card_strength = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10,
    #             '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    # types = {}
    # for hand in hands_ranked:
    #     types[hand] = get_hand_type(hand, with_joker = False)

    # PART 2
    card_strength = {'A':14, 'K':13, 'Q':12, 'T':10,
                '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J':1}
    types = {}
    for hand in hands_ranked:
        types[hand] = get_hand_type(hand, with_joker = True)

    # PART 1 + 2
    compare_key = cmp_to_key(compare)
    hands_ranked = sorted(hands_ranked, key=compare_key)
    total_winnings = 0
    for n, hand in enumerate(hands_ranked):
        # the win of each card is the product of its bid and its rank
        total_winnings += hands[hand]*(n+1)
    print(total_winnings)
