def count_cards(hand):
    card_count = {}

    for card in hand:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1

    return card_count


def get_type(card_count):
    TYPES = {
        "High card": 1,
        "One pair": 2,
        "Two pair": 3,
        "Three of a kind": 4,
        "Full house": 5,
        "Four of a kind": 6,
        "Five of a kind": 7
    }

    max_count = max(card_count.values())

    # The length of card_count is the number of unique cards in the hand
    if len(card_count) == 1:
        return TYPES["Five of a kind"]
    elif len(card_count) == 2:
        if max_count == 4:
            return TYPES["Four of a kind"]
        elif max_count == 3:
            return TYPES["Full house"]
    elif len(card_count) == 3:
        if max_count == 3:
            return TYPES["Three of a kind"]
        elif max_count == 2:
            return TYPES["Two pair"]
    elif len(card_count) == 4:
        return TYPES["One pair"]
    else:
        return TYPES["High card"]


def is_hand_sorted(hand_a, hand_b):
    LABELS = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}

    type_a, type_b = get_type(count_cards(hand_a)), get_type(count_cards(hand_b))
    label_a, label_b = LABELS[hand_a[0]], LABELS[hand_b[0]]

    if type_a == type_b:
        i = 0
        label_a, label_b = LABELS[hand_a[i]], LABELS[hand_b[i]]
        while label_a == label_b:
            i += 1
            label_a, label_b = LABELS[hand_a[i]], LABELS[hand_b[i]]
        return label_a < label_b
    return type_a < type_b


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    midpoint = len(arr) // 2
    left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    result = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if is_hand_sorted(left[l], right[r]):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    while l < len(left):
        result.append(left[l])
        l += 1
    
    while r < len(right):
        result.append(right[r])
        r += 1

    return result


def part1(data):
    arr = [line.split()[0] for line in data]
    sorted_hands = merge_sort(arr)

    hand_to_bid = {}
    for line in data:
        hand, bid = line.split()
        hand_to_bid[hand] = int(bid)

    result = 0
    for i in range(len(sorted_hands)):
        result += hand_to_bid[sorted_hands[i]] * (i + 1)
    
    return result


with open("../inputs/day7.txt") as file:
    data = file.read().strip().split("\n")
    part1 = part1(data)
    # part2 = part2(data)
    print(f"Part 1: {part1}")
    # print(f"Part 2: {part2}")
