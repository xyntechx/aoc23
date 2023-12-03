def part1(data):
    result = 0

    for i in range(len(data)):
        line = data[i]
        sets = line.split(":")[-1].strip().split("; ")
        impossible = 0

        for s in sets:
            balls = map(lambda x: x.split(), s.split(", "))
            for b in balls:
                if (b[-1] == "red" and int(b[0]) > 12) or (b[-1] == "green" and int(b[0]) > 13) or (b[-1] == "blue" and int(b[0]) > 14):
                    impossible += 1

        if impossible == 0:
            result += i + 1

    return result


def part2(data):
    sum_of_powers = 0

    for line in data:
        red, green, blue = [], [], []

        sets = line.split(":")[-1].strip().split("; ")

        for s in sets:
            balls = map(lambda x: x.split(), s.split(", "))
            for b in balls:
                if b[-1] == "red":
                    red.append(int(b[0]))
                elif b[-1] == "green":
                    green.append(int(b[0]))
                elif b[-1] == "blue":
                    blue.append(int(b[0]))

        sum_of_powers += max(red) * max(green) * max(blue)

    return sum_of_powers


with open("../inputs/day2.txt") as file:
    data = file.read().strip().split("\n")
    part1 = part1(data)
    part2 = part2(data)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
