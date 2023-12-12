import math


def find_empty_rows_columns():
    global input_map
    empty_rows = []
    empty_columns = []
    for k in range(len(input_map)):
        has_galaxy = False
        for char in input_map[k]:
            if char == '#':
                has_galaxy = True
        if not has_galaxy:
            empty_rows.append(k)
    for k in range(len(input_map[0])):
        has_galaxy = False
        for row in input_map:
            if row[k] == '#':
                has_galaxy = True
        if not has_galaxy:
            empty_columns.append(k)
    return empty_rows, empty_columns


def find_galaxy_positions():
    global input_map
    positions = []
    for k in range(len(input_map)):
        for j in range(len(input_map[0])):
            if input_map[k][j] == '#':
                positions.append((k, j))
    return positions


if __name__ == "__main__":
    with open('input.txt') as f:
        input_map = f.read().split('\n')
    rows, columns = find_empty_rows_columns()
    galaxy_positions = find_galaxy_positions()
    distance = 0
    for k in range(len(galaxy_positions)):
        for j in range(k + 1, len(galaxy_positions)):
            expansion = 0
            for row in rows:
                if galaxy_positions[k][0] <= row <= galaxy_positions[j][0] or galaxy_positions[j][0] <= row <= \
                        galaxy_positions[k][0]:
                    expansion += 1
            for column in columns:
                if galaxy_positions[k][1] <= column <= galaxy_positions[j][1] or galaxy_positions[j][1] <= column <= \
                        galaxy_positions[k][1]:
                    expansion += 1
            distance += expansion + math.fabs(galaxy_positions[j][0] - galaxy_positions[k][0]) + math.fabs(
                galaxy_positions[j][1] - galaxy_positions[k][1])
    print(f"Part 1: {int(distance)}")

    rows, columns = find_empty_rows_columns()
    galaxy_positions = find_galaxy_positions()
    distance = 0
    for k in range(len(galaxy_positions)):
        for j in range(k + 1, len(galaxy_positions)):
            expansion = 0
            for row in rows:
                if galaxy_positions[k][0] <= row <= galaxy_positions[j][0] or galaxy_positions[j][0] <= row <= \
                        galaxy_positions[k][0]:
                    expansion += 10 ** 6 - 1
            for column in columns:
                if galaxy_positions[k][1] <= column <= galaxy_positions[j][1] or galaxy_positions[j][1] <= column <= \
                        galaxy_positions[k][1]:
                    expansion += 10 ** 6 - 1
            distance += expansion + math.fabs(galaxy_positions[j][0] - galaxy_positions[k][0]) + math.fabs(
                galaxy_positions[j][1] - galaxy_positions[k][1])
    print(f"Part 2: {int(distance)}")
