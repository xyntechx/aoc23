def get_destination(source, arr):
    result = list(filter(lambda e: e[1] <= source < e[1] + e[2], arr))

    if not result:
        return source # source index == dest index

    dest_start, source_start, _ = result[0]
    diff = source - source_start
    dest = dest_start + diff

    return dest


def get_source(dest, arr):
    result = list(filter(lambda e: e[0] <= dest < e[0] + e[2], arr))

    if not result:
        return dest # source index == dest index

    dest_start, source_start, _ = result[0]
    diff = dest - dest_start
    source = source_start + diff

    return source


def part1(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location):
    seed_to_location = [[s, None] for s in seeds]

    for i in range(len(seeds)):
        soil = get_destination(seeds[i], seed_to_soil)
        fertilizer = get_destination(soil, soil_to_fertilizer)
        water = get_destination(fertilizer, fertilizer_to_water)
        light = get_destination(water, water_to_light)
        temperature = get_destination(light, light_to_temperature)
        humidity = get_destination(temperature, temperature_to_humidity)
        location = get_destination(humidity, humidity_to_location)

        seed_to_location[i][1] = location

    return min(seed_to_location, key=lambda e: e[1])[1]


def part2(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location):
    # for 1st iteration, find min of all start locations
    hum_loc = min(humidity_to_location, key=lambda e: e[0])
    loc, loc_end = hum_loc[0], hum_loc[0] + hum_loc[2]

    while True:
        humidity = get_source(loc, humidity_to_location)
        temperature = get_source(humidity, temperature_to_humidity)
        light = get_source(temperature, light_to_temperature)
        water = get_source(light, water_to_light)
        fertilizer = get_source(water, fertilizer_to_water)
        soil = get_source(fertilizer, soil_to_fertilizer)
        seed = get_source(soil, seed_to_soil)

        for seed_index in range(len(seeds) // 2):
            seed_start, seed_stop = seeds[seed_index * 2], seeds[seed_index * 2] + seeds[seed_index * 2 + 1]
            if seed_start <= seed < seed_stop:
                return loc

        loc += 1
        if loc == loc_end:
            # location has exceeded range; change hum_loc group
            humidity_to_location.remove(hum_loc) # so that this won't be selected again (prevent infinite loop)
            hum_loc = min(humidity_to_location, key=lambda e: e[0])
            loc, loc_end = hum_loc[0], hum_loc[0] + hum_loc[2]


with open("../inputs/day5.txt") as file:
    data = file.read().strip().split("\n")
    args = [[], [], [], [], [], [], [], []]
    curr_args_index = 1

    args[0].extend(list(map(int, data[0].split(":")[1].strip().split(" "))))

    for line in data[2:]:
        match line.strip():
            case "seed-to-soil map:":
                curr_args_index = 1
            case "soil-to-fertilizer map:":
                curr_args_index = 2
            case "fertilizer-to-water map:":
                curr_args_index = 3
            case "water-to-light map:":
                curr_args_index = 4
            case "light-to-temperature map:":
                curr_args_index = 5
            case "temperature-to-humidity map:":
                curr_args_index = 6
            case "humidity-to-location map:":
                curr_args_index = 7
            case "":
                pass
            case _:
                arg = list(map(int, line.strip().split(" ")))
                args[curr_args_index].append(arg)

    part1_res = part1(*args)
    part2_res = part2(*args)
    print(f"Part 1: {part1_res}")
    print(f"Part 2: {part2_res}")
