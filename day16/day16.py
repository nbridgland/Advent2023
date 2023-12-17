def follow_beam(x, y, direction):
    global mirror_map
    global energized_map
    while 0 <= x < len(mirror_map[0]) and 0 <= y < len(mirror_map):
        if direction in energized_map[y][x]:
            break
        energized_map[y][x] += direction
        if direction == '>':
            if mirror_map[y][x] == "\\":
                direction = 'v'
                y += 1
            elif mirror_map[y][x] == "/":
                direction = '^'
                y -= 1
            elif mirror_map[y][x] == "|":
                follow_beam(x, y - 1, '^')
                follow_beam(x, y + 1, 'v')
                break
            else:
                x += 1
        elif direction == '<':
            if mirror_map[y][x] == "\\":
                direction = '^'
                y -= 1
            elif mirror_map[y][x] == "/":
                direction = 'v'
                y += 1
            elif mirror_map[y][x] == "|":
                follow_beam(x, y - 1, '^')
                follow_beam(x, y + 1, 'v')
                break
            else:
                x -= 1
        elif direction == '^':
            if mirror_map[y][x] == "\\":
                direction = '<'
                x -= 1
            elif mirror_map[y][x] == "/":
                direction = '>'
                x += 1
            elif mirror_map[y][x] == "-":
                follow_beam(x + 1, y, '>')
                follow_beam(x - 1, y, '<')
                break
            else:
                y -= 1
        elif direction == 'v':
            if mirror_map[y][x] == "\\":
                direction = '>'
                x += 1
            elif mirror_map[y][x] == "/":
                direction = '<'
                x -= 1
            elif mirror_map[y][x] == "-":
                follow_beam(x + 1, y, '>')
                follow_beam(x - 1, y, '<')
                break
            else:
                y += 1


def count_energized():
    global energized_map
    output = 0
    for line in energized_map:
        for entry in line:
            if entry:
                output += 1
    return output


if __name__ == "__main__":
    with open('input.txt') as f:
        mirror_map = f.read().split('\n')
    energized_map = [['' for k in range(len(mirror_map[0]))] for j in range(len(mirror_map))]
    follow_beam(0, 0, '>')
    energized = count_energized()
    print(f"Part 1: {energized}")

    to_check = ([(0, y, '>') for y in range(len(mirror_map))] +
                [(len(mirror_map[0]) - 1, y, '<') for y in range(len(mirror_map))] +
                [(x, 0, 'v') for x in range(len(mirror_map[0]))] +
                [(x, len(mirror_map) - 1, '^') for x in range(len(mirror_map[0]))])

    max_energized = 0
    while len(to_check) > 0:
        energized_map = [['' for k in range(len(mirror_map[0]))] for j in range(len(mirror_map))]
        start_pos = to_check[0]
        follow_beam(*start_pos)
        max_energized = max(max_energized, count_energized())
        to_check = [start_pos for start_pos in to_check if
                    start_pos[2] not in energized_map[start_pos[1]][start_pos[0]]]
    print(f"Part 2: {max_energized}")
