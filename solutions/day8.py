from math import lcm


def part1(instructions, node_to_lr, curr_node="AAA", end_cond=lambda e: e == "ZZZ"):
    num_steps = 0
    instr_index = 0

    while not end_cond(curr_node):
        instr = instructions[instr_index]
        if instr == "L":
            curr_node = node_to_lr[curr_node][0]
        else:
            curr_node = node_to_lr[curr_node][1]

        num_steps += 1

        instr_index += 1
        if instr_index == len(instructions):
            instr_index = 0

    return num_steps


def part2(instructions, node_to_lr):
    num_steps_arr = []

    for node in node_to_lr:
        if node[2] == "A":
            num_steps_arr.append(part1(instructions, node_to_lr, curr_node=node, end_cond=lambda e: e[2] == "Z"))

    return lcm(*num_steps_arr)


with open("../inputs/day8.txt") as file:
    data = file.read().strip().split("\n")

    instructions = data[0]

    node_to_lr = {}
    for line in data[2:]:
        node, lr = line.split(" = ")
        l, r = lr.split(",")
        node_to_lr[node] = (l[1:], r[1:len(r)-1])

    part1_res = part1(instructions, node_to_lr)
    part2_res = part2(instructions, node_to_lr)
    print(f"Part 1: {part1_res}")
    print(f"Part 2: {part2_res}")
