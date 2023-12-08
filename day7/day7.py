card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
alt_card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def build_card_dict(cards):
    card_dict = {}
    for card in cards:
        if card in card_dict:
            card_dict[card] += 1
        else:
            card_dict[card] = 1
    return card_dict


def get_hand_type(cards):
    card_dict = build_card_dict(cards)
    if len(card_dict) == 1:
        return 7
    if len(card_dict) == 2:
        if max(card_dict.values()) == 4:
            return 6
        return 5
    if len(card_dict) == 3:
        if max(card_dict.values()) == 3:
            return 4
        return 3
    if len(card_dict) == 4:
        return 2
    return 1


def alt_get_hand_type(cards):
    if 'J' not in cards:
        return get_hand_type(cards)
    card_dict = build_card_dict(cards)
    j = card_dict['J']
    del card_dict['J']
    if len(card_dict) == 0:  # maybe they're all Js
        return 7
    if len(card_dict) == 1:
        return 7
    if len(card_dict) == 2:
        if max(card_dict.values()) + j == 4:
            return 6
        return 5
    if len(card_dict) == 3:
        if max(card_dict.values()) + j == 3:
            return 4
        return 3
    return 2


class Hand:
    def __init__(self, input_line):
        self.cards, self.bid = input_line.split(' ')
        self.hand_type = get_hand_type(self.cards)
        self.rank = 1

    def compare(self, hand2):
        if self.hand_type < hand2.hand_type:
            return 0
        if self.hand_type > hand2.hand_type:
            return 1
        for k in range(5):
            if card_order.index(self.cards[k]) < card_order.index(hand2.cards[k]):
                return 1
            if card_order.index(self.cards[k]) > card_order.index(hand2.cards[k]):
                return 0


class AltHand:
    def __init__(self, input_line):
        self.cards, self.bid = input_line.split(' ')
        self.hand_type = alt_get_hand_type(self.cards)
        self.rank = 1

    def compare(self, hand2):
        if self.hand_type < hand2.hand_type:
            return 0
        if self.hand_type > hand2.hand_type:
            return 1
        for k in range(5):
            if alt_card_order.index(self.cards[k]) < alt_card_order.index(hand2.cards[k]):
                return 1
            if alt_card_order.index(self.cards[k]) > alt_card_order.index(hand2.cards[k]):
                return 0


if __name__ == "__main__":
    with open('input.txt') as f:
        hands = [Hand(hand) for hand in f.read().split('\n')]
    for k in range(len(hands)):
        for j in range(k + 1, len(hands)):
            if hands[k].compare(hands[j]):
                hands[k].rank += 1
            else:
                hands[j].rank += 1
    print(f"Part 1: {sum([hand.rank * int(hand.bid) for hand in hands])}")

    with open('input.txt') as f:
        hands = [AltHand(hand) for hand in f.read().split('\n')]
    for k in range(len(hands)):
        for j in range(k + 1, len(hands)):
            if hands[k].compare(hands[j]):
                hands[k].rank += 1
            else:
                hands[j].rank += 1
    print(f"Part 2: {sum([hand.rank * int(hand.bid) for hand in hands])}")
