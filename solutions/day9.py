def part1(data):
    result = 0

    for line in data:
        nums = list(map(int, line.split()))
        diffs = [b - a for b, a in zip(nums[1:], nums)]
        last_nums = [nums[-1]]

        while not all(map(lambda n: n == 0, diffs)):
            nums = diffs[:]
            diffs = [b - a for b, a in zip(nums[1:], nums)]
            last_nums.append(nums[-1])

        result += sum(last_nums)

    return result


def part2(data):
    new_data = [' '.join(reversed(line.split())) for line in data]
    return part1(new_data)


with open("../inputs/day9.txt") as file:
    data = file.read().strip().split("\n")
    part1_res = part1(data)
    part2_res = part2(data)
    print(f"Part 1: {part1_res}")
    print(f"Part 2: {part2_res}")
