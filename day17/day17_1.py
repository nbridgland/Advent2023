import time


def clean_entry(dictionary_entry):
    output = {}
    for direction in dictionary_entry:
        output[direction] = []
        for k in range(len(dictionary_entry[direction])):
            pair1 = dictionary_entry[direction][k]
            flagged = False
            for j in range(len(dictionary_entry[direction])):
                pair2 = dictionary_entry[direction][j]
                if pair2[0] < pair1[0] and pair2[1] <= pair1[1] or pair2[1] < pair1[1] and pair2[0] <= pair1[0]:
                    flagged = True
                if pair1 == pair2 and j < k:
                    flagged = True
                if pair1[1] == 4:
                    flagged = True
            if not flagged:
                output[direction].append(pair1)
    return output


def find_min(entry):
    min_entry = 10**9
    for direction in entry:
        for pair in entry[direction]:
            if pair[0] < min_entry:
                min_entry = pair[0]
    return min_entry


def update_path_map(update_x, update_y, from_direction):
    global path_map
    current_entry = path_map[update_y][update_x]
    temp_entry = {key: [item for item in path_map[update_y][update_x][key]] for key in path_map[update_y][update_x]}
    if from_direction == '<':
        if '<' not in temp_entry:
            temp_entry['<'] = []
        for direction in path_map[update_y][update_x + 1]:
            if direction == '<':
                temp_entry['<'] += [(pair[0] + city_map[update_y][update_x], pair[1] + 1)
                                    for pair in path_map[update_y][update_x + 1][direction]]
            elif direction == '>':
                pass
            else:
                temp_entry['<'] += [(pair[0] + city_map[update_y][update_x], 1)
                                    for pair in path_map[update_y][update_x + 1][direction]]
        path_map[update_y][update_x] = clean_entry(temp_entry)
        if path_map[update_y][update_x] != current_entry:
            if update_y > 0 and path_map[update_y-1][update_x]:
                update_path_map(update_x, update_y - 1, '^')
            if update_y < len(city_map) - 1 and path_map[update_y + 1][update_x]:
                update_path_map(update_x, update_y + 1, 'v')
            if update_x > 0 and path_map[update_y][update_x - 1]:
                update_path_map(update_x - 1, update_y, '<')
    if from_direction == '>':
        if '>' not in temp_entry:
            temp_entry['>'] = []
        for direction in path_map[update_y][update_x - 1]:
            if direction == '>':
                temp_entry['>'] += [(pair[0] + city_map[update_y][update_x], pair[1] + 1)
                                    for pair in path_map[update_y][update_x - 1][direction]]
            elif direction == '<':
                pass
            else:
                temp_entry['>'] += [(pair[0] + city_map[update_y][update_x], 1)
                                    for pair in path_map[update_y][update_x - 1][direction]]
        path_map[update_y][update_x] = clean_entry(temp_entry)
        if path_map[update_y][update_x] != current_entry:
            if update_y > 0 and path_map[update_y - 1][update_x]:
                update_path_map(update_x, update_y - 1, '^')
            if update_y < len(city_map) - 1 and path_map[update_y + 1][update_x]:
                update_path_map(update_x, update_y + 1, 'v')
            if update_x < len(city_map) - 1 and path_map[update_y][update_x + 1]:
                update_path_map(update_x + 1, update_y, '>')
    if from_direction == 'v':
        if 'v' not in temp_entry:
            temp_entry['v'] = []
        for direction in path_map[update_y - 1][update_x]:
            if direction == 'v':
                temp_entry['v'] += [(pair[0] + city_map[update_y][update_x], pair[1] + 1)
                                    for pair in path_map[update_y - 1][update_x][direction]]
            elif direction == '^':
                pass
            else:
                temp_entry['v'] += [(pair[0] + city_map[update_y][update_x], 1)
                                    for pair in path_map[update_y - 1][update_x][direction]]
        path_map[update_y][update_x] = clean_entry(temp_entry)
        if path_map[update_y][update_x] != current_entry:
            if update_y < len(city_map) - 1 and path_map[update_y+1][update_x]:
                update_path_map(update_x, update_y + 1, 'v')
            if update_x > 0 and path_map[update_y][update_x-1]:
                update_path_map(update_x - 1, update_y, '<')
            if update_x < len(city_map) - 1 and path_map[update_y][update_x + 1]:
                update_path_map(update_x + 1, update_y, '>')
    if from_direction == '^':
        if '^' not in temp_entry:
            temp_entry['^'] = []
        for direction in path_map[update_y + 1][update_x]:
            if direction == '^':
                temp_entry['^'] += [(pair[0] + city_map[update_y][update_x], pair[1] + 1)
                                    for pair in path_map[update_y + 1][update_x][direction]]
            elif direction == 'v':
                pass
            else:
                temp_entry['^'] += [(pair[0] + city_map[update_y][update_x], 1)
                                    for pair in path_map[update_y + 1][update_x][direction]]
        path_map[update_y][update_x] = clean_entry(temp_entry)
        if path_map[update_y][update_x] != current_entry:
            if update_y > 0 and path_map[update_y-1][update_x]:
                update_path_map(update_x, update_y - 1, '^')
            if update_x > 0 and path_map[update_y][update_x-1]:
                update_path_map(update_x - 1, update_y, '<')
            if update_x < len(city_map) - 1 and path_map[update_y][update_x + 1]:
                update_path_map(update_x + 1, update_y, '>')


if __name__ == "__main__":
    tick = time.time()
    with open('input.txt') as f:
        city_map = f.read().split('\n')
    city_map = [[int(char) for char in line] for line in city_map]
    path_map = [[{} for char in line] for line in city_map]
    path_map[0][0] = {'>': [(0, 0)], 'v': [(0, 0)]} #direction: (accumulated_heat, n_steps), only store best two directions
    current_corner = 0
    while current_corner + 1 < len(city_map):
        # deal with the top-right corner
        temp_entry = {'>': []}
        for direction in path_map[0][current_corner]:
            if direction == '>':
                for pair in path_map[0][current_corner][direction]:
                    temp_entry[direction].append((pair[0] + city_map[0][current_corner+1], pair[1]+1))
            elif direction == '<':
                pass
            else:
                for pair in path_map[0][current_corner][direction]:
                    temp_entry['>'].append((pair[0] + city_map[0][current_corner+1], 1))
        path_map[0][current_corner + 1] = clean_entry(temp_entry)

        #do the whole right side to corner
        for y in range(1, current_corner + 1):
            temp_entry = {'>': [], 'v': []}
            for direction in path_map[y][current_corner]:
                if direction == '>':
                    for pair in path_map[y][current_corner][direction]:
                        temp_entry[direction].append((pair[0] + city_map[y][current_corner + 1], pair[1] + 1))
                elif direction == '<':
                    pass
                else:
                    for pair in path_map[y][current_corner][direction]:
                        temp_entry['>'].append((pair[0] + city_map[y][current_corner + 1], 1))
            for direction in path_map[y-1][current_corner+1]:
                if direction == 'v':
                    for pair in path_map[y-1][current_corner+1][direction]:
                        temp_entry[direction].append((pair[0] + city_map[y][current_corner + 1], pair[1] + 1))
                elif direction == '^':
                    pass
                else:
                    for pair in path_map[y-1][current_corner+1][direction]:
                        temp_entry['v'].append((pair[0] + city_map[y][current_corner + 1], 1))
            path_map[y][current_corner + 1] = clean_entry(temp_entry)

        #and top right corner from below:
        temp_entry = path_map[0][current_corner + 1]
        for direction in path_map[1][current_corner+1]:
            if direction == '^':
                if '^' not in temp_entry:
                    temp_entry['^'] = []
                for pair in path_map[1][current_corner+1][direction]:
                    temp_entry[direction].append((pair[0] + city_map[0][current_corner+1], pair[1]+1))
            elif direction == 'v':
                pass
            else:
                if '^' not in temp_entry:
                    temp_entry['^'] = []
                for pair in path_map[1][current_corner+1][direction]:
                    temp_entry['^'].append((pair[0] + city_map[0][current_corner+1], 1))
        path_map[0][current_corner + 1] = clean_entry(temp_entry)

        #do the bottom-left corner
        temp_entry = {'v': []}
        for direction in path_map[current_corner][0]:
            if direction == 'v':
                for pair in path_map[current_corner][0][direction]:
                    temp_entry[direction].append((pair[0] + city_map[current_corner+1][0], pair[1]+1))
            elif direction == '^':
                pass
            else:
                for pair in path_map[current_corner][0][direction]:
                    temp_entry['v'].append((pair[0] + city_map[current_corner+1][0], 1))
        path_map[current_corner + 1][0] = clean_entry(temp_entry)

        #do the bottom side through corner
        for x in range(1, current_corner + 2):
            temp_entry = {'v': [], '>': []}
            for direction in path_map[current_corner][x]:
                if direction == 'v':
                    for pair in path_map[current_corner][x][direction]:
                        temp_entry[direction].append((pair[0] + city_map[current_corner + 1][x], pair[1] + 1))
                elif direction == '^':
                    pass
                else:
                    for pair in path_map[current_corner][x][direction]:
                        temp_entry['v'].append((pair[0] + city_map[current_corner + 1][x], 1))
            for direction in path_map[current_corner+1][x-1]:
                if direction == '>':
                    for pair in path_map[current_corner+1][x-1][direction]:
                        temp_entry[direction].append((pair[0] + city_map[current_corner + 1][x], pair[1] + 1))
                elif direction == '<':
                    pass
                else:
                    for pair in path_map[current_corner+1][x-1][direction]:
                        temp_entry['>'].append((pair[0] + city_map[current_corner + 1][x], 1))
            path_map[current_corner + 1][x] = clean_entry(temp_entry)

        # and bottom left from the right
        temp_entry = path_map[current_corner + 1][0]
        if '<' not in temp_entry:
            temp_entry['<'] = []
        for direction in path_map[current_corner+1][1]:
            if direction == '<':
                for pair in path_map[current_corner + 1][1][direction]:
                    temp_entry[direction].append((pair[0] + city_map[current_corner+1][0], pair[1]+1))
            elif direction == '>':
                pass
            else:
                for pair in path_map[current_corner + 1][1][direction]:
                    temp_entry['<'].append((pair[0] + city_map[current_corner+1][0], 1))
        path_map[current_corner + 1][0] = clean_entry(temp_entry)

        #check if interior needs updating
        for x in range(current_corner):
            update_path_map(x, current_corner, 'v')
        for y in range(current_corner):
            update_path_map(current_corner, y, from_direction='<')
        current_corner += 1
    print(f"Part 1: {find_min(path_map[-1][-1])}")
    tock = time.time()
    print(tock - tick)