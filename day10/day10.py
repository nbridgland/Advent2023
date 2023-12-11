north_pipes = ['|', 'L', 'J']
south_pipes = ['|', '7', 'F']
east_pipes = ['-', 'L', 'F']
west_pipes = ['-', 'J', '7']


def find_s():
    global input_map
    for k in range(len(input_map)):
        for j in range(len(input_map[k])):
            if input_map[k][j] == 'S':
                return k, j


def get_possible_directions(y, x, max_down, max_right):
    input_char = input_map[y][x]
    output = []
    if input_char == 'S':
        if y > 0:
            output.append('north')
        if y < max_down - 1:
            output.append('south')
        if x > 0:
            output.append('west')
        if x < max_right - 1:
            output.append('east')
        return output
    if input_char in north_pipes:
        output.append('north')
    if input_char in south_pipes:
        output.append('south')
    if input_char in east_pipes:
        output.append('east')
    if input_char in west_pipes:
        output.append('west')
    return output


def traverse_map(pos):
    y = pos[0]
    x = pos[1]
    global input_map, output_map, starting_positions
    directions = get_possible_directions(y, x, len(input_map), len(input_map[0]))
    for direction in directions:
        if direction == 'north':
            if output_map[y - 1][x] == '.':
                if input_map[y - 1][x] in south_pipes:
                    output_map[y - 1][x] = output_map[y][x] + 1
                    starting_positions.append((y - 1, x))
        if direction == 'south':
            if output_map[y + 1][x] == '.':
                if input_map[y + 1][x] in north_pipes:
                    output_map[y + 1][x] = output_map[y][x] + 1
                    starting_positions.append((y + 1, x))
        if direction == 'west':
            if output_map[y][x - 1] == '.':
                if input_map[y][x - 1] in east_pipes:
                    output_map[y][x - 1] = output_map[y][x] + 1
                    starting_positions.append((y, x - 1))
        if direction == 'east':
            if output_map[y][x + 1] == '.':
                if input_map[y][x + 1] in west_pipes:
                    output_map[y][x + 1] = output_map[y][x] + 1
                    starting_positions.append((y, x + 1))


def replace_int(thing):
    if type(thing) is int:
        return 'O'
    return thing


def expand_map(compressed_map):
    expanded_map = []
    for line in compressed_map:
        new_line = [replace_int(thing) for thing in line]
        expanded_map.append([char for char in ','.join(new_line)])
        expanded_map.append([',' for k in range(len(expanded_map[0]))])
    return expanded_map


def is_open_adjacent(y, x):
    if y > 0:
        if expanded_counters[y - 1][x] == '0':
            return True
    if y < len(expanded_counters) - 1:
        if expanded_counters[y + 1][x] == '0':
            return True
    if x > 0:
        if expanded_counters[y][x - 1] == '0':
            return True
    if x < len(expanded_counters[0]) - 1:
        if expanded_counters[y][x + 1] == '0':
            return True


if __name__ == "__main__":
    with open('input.txt') as f:
        input_map = f.read().split('\n')
    output_map = [['.' for k in range(len(line))] for line in input_map]
    starting_positions = [find_s()]
    output_map[starting_positions[0][0]][starting_positions[0][1]] = 0
    k = 0
    while k < len(starting_positions):
        traverse_map(starting_positions[k])
        k += 1
    part_two_map = [[char for char in line] for line in output_map]
    for k in range(len(output_map)):
        for j in range(len(output_map[0])):
            if output_map[k][j] == '.':
                output_map[k][j] = 0
    print(f"Part 1: {max([max([char for char in line]) for line in output_map])}")

    expanded_counters = expand_map(part_two_map)
    expanded_pipes = expand_map(input_map)
    for k in range(len(expanded_counters)):
        for j in range(len(expanded_counters[0])):
            if expanded_counters[k][j] == 'O':
                if expanded_pipes[k][j] in north_pipes:
                    expanded_counters[k - 1][j] = '|'
                if expanded_pipes[k][j] in south_pipes:
                    expanded_counters[k + 1][j] = '|'
                if expanded_pipes[k][j] in east_pipes:
                    expanded_counters[k][j + 1] = '-'
                if expanded_pipes[k][j] in west_pipes:
                    expanded_counters[k][j - 1] = '-'

    expanded_counters[0][0] = '0'  # cheated a little and looked
    updated = True
    while updated:
        updated = False
        for k in range(len(expanded_counters)):
            for j in range(len(expanded_counters[0])):
                if expanded_counters[k][j] in ['.', ',']:
                    if is_open_adjacent(k, j):
                        expanded_counters[k][j] = '0'
                        updated = True
    count_interior = 0
    for line in expanded_counters:
        for char in line:
            if char == '.':
                count_interior += 1

    print(f"Part 2: {count_interior}")
