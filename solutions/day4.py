def part1(data):
    result = 0

    for row in data:
        nums = row.split(":")[1].strip().split("|")
        winning_nums, my_nums = list(map(int, nums[0].strip().split())), list(map(int, nums[1].strip().split()))
        intersection = [num for num in winning_nums if num in my_nums]
        if intersection:
            result += 2 ** (len(intersection) - 1)

    return result


def part2(data):
    card_to_count = {}

    for card_index in range(len(data)):
        card_to_count[card_index + 1] = 1 # init all cards to have count of 1

    for card_index in range(len(data)):
        nums = data[card_index].split(":")[1].strip().split("|")
        winning_nums, my_nums = list(map(int, nums[0].strip().split())), list(map(int, nums[1].strip().split()))
        intersection = [num for num in winning_nums if num in my_nums]
        num_of_matches = len(intersection)

        for i in range(card_index + 2, card_index + 2 + num_of_matches):
            if i in card_to_count:
                card_to_count[i] += card_to_count[card_index + 1]
            else:
                card_to_count[i] = card_to_count[card_index + 1]

    return sum(card_to_count.values())


with open("../inputs/day4.txt") as file:
    data = file.read().strip().split("\n")
    part1 = part1(data)
    part2 = part2(data)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
