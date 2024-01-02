from math import sqrt, floor, ceil


def get_count(T, D):
    t2 = floor((T + sqrt(T*T - 4*D)) / 2)
    t1 = ceil((T - sqrt(T*T - 4*D)) / 2)
    return t2 - t1 + 1


def part1(times, distances):
    result = 1

    for i in range(len(times)):
        T = times[i]
        D = distances[i] + 1
        result *= get_count(T, D)

    return result


def part2(times, distances):
    T = int("".join([str(t) for t in times]))
    D = int("".join([str(d) for d in distances])) + 1
    return get_count(T, D)


with open("../inputs/day6.txt") as file:
    data = file.read().strip().split("\n")
    times, distances = map(lambda e: list(map(int, ' '.join(e.split(":")[1].strip().split()).split())), data)

    part1 = part1(times, distances)
    part2 = part2(times, distances)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
