def part1(times, distances):
    result = 1

    for i in range(len(times)):
        count = 0
        T = times[i]
        D = distances[i]

        for t in range(T + 1):
            my_distance = (T - t) * t
            if my_distance > D:
                count += 1
            elif my_distance <= D and count > 0:
                break

        result *= count

    return result


def part2(times, distances):
    count = 0

    T = int("".join([str(t) for t in times]))
    D = int("".join([str(d) for d in distances]))

    for t in range(T + 1):
        my_distance = (T - t) * t
        if my_distance > D:
            count += 1
        elif my_distance <= D and count > 0:
            break

    return count


with open("../inputs/day6.txt") as file:
    data = file.read().strip().split("\n")
    times, distances = map(lambda e: list(map(int, ' '.join(e.split(":")[1].strip().split()).split())), data)

    part1 = part1(times, distances)
    part2 = part2(times, distances)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
