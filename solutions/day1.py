def get_calibration_values(line):
    digits = []

    for char in line:
        if char.isdigit():
            digits.append(int(char))

    return digits[0]*10 + digits[-1]


def part1(data):
    result = 0

    for line in data:
        result += get_calibration_values(line)

    return result


def part2(data):
    NUMBERS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    result = 0

    for line in data:
        for num in NUMBERS:
            line = line.replace(num, f"{num}{NUMBERS[num]}{num}")

        result += get_calibration_values(line)

    return result


with open("../inputs/day1.txt") as file:
    data = file.read().split()
    part1 = part1(data)
    part2 = part2(data)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
