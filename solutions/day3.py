def part1(data):
    OFFSETS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    is_digit = False
    saved_digit_coords = []
    saved_num = 0

    result = 0

    for row_index in range(len(data)):
        line = data[row_index]

        for col_index in range(len(line)):
            char = line[col_index]

            if char.isdigit():
                is_digit = True
                saved_digit_coords.append((row_index, col_index))
                saved_num = saved_num * 10 + int(char)

            if not char.isdigit() or col_index == len(line) - 1:
                if is_digit:
                    for d in saved_digit_coords:
                        for o in OFFSETS:
                            r, c, o_r, o_c = d[0], d[1], o[0], o[1]
                            try:
                                surrounding = data[r + o_r][c + o_c]
                                if surrounding != "." and not surrounding.isdigit():
                                    result += saved_num
                                    is_digit = False
                                    saved_digit_coords = []
                                    saved_num = 0
                                    break
                            except IndexError:
                                continue
                        else:
                            continue
                        break
                    else:
                        is_digit = False
                        saved_digit_coords = []
                        saved_num = 0

    return result


def part2(data):
    OFFSETS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    is_digit = False
    saved_digit_coords = []
    saved_num = 0

    star_to_nums = {} # coords of star: list of numbers around it

    result = 0

    # Initialize star_to_nums with all the stars
    for row_index in range(len(data)):
        line = data[row_index]

        for col_index in range(len(line)):
            char = line[col_index]

            if char == "*":
                star_to_nums[(row_index, col_index)] = []

    # Iterating through data for any numbers
    for row_index in range(len(data)):
        line = data[row_index]

        for col_index in range(len(line)):
            char = line[col_index]

            if char.isdigit():
                is_digit = True
                saved_digit_coords.append((row_index, col_index))
                saved_num = saved_num * 10 + int(char)

            if not char.isdigit() or col_index == len(line) - 1:
                if is_digit:
                    for d in saved_digit_coords:
                        for o in OFFSETS:
                            r, c, o_r, o_c = d[0], d[1], o[0], o[1]
                            try:
                                surrounding = data[r + o_r][c + o_c]
                                if surrounding == "*":
                                    star_to_nums[(r + o_r, c + o_c)].append(saved_num)
                                    is_digit = False
                                    saved_digit_coords = []
                                    saved_num = 0
                                    break
                            except IndexError:
                                continue
                        else:
                            continue
                        break
                    else:
                        is_digit = False
                        saved_digit_coords = []
                        saved_num = 0

    # Check if star is a gear
    for nums in star_to_nums.values():
        if len(nums) == 2:
            result += nums[0] * nums[1]

    return result


with open("../inputs/day3.txt") as file:
    data = file.read().strip().split("\n")
    part1 = part1(data)
    part2 = part2(data)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
