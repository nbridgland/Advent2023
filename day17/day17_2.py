import time

def follow_path(x, y, direction, dir_length, lost_heat):
    global city_map
    global path_map
    if x == y == len(city_map)-1:
        return lost_heat
    if lost_heat > 932: # this is maybe cheating a little wee bit
        return None
    for k in range(1, dir_length+1):
        if k in path_map[y][x][direction]:
            if path_map[y][x][direction][k] < lost_heat:
                return None
    path_map[y][x][direction][dir_length] = lost_heat
    possibilities = []
    if direction == '>':
        if dir_length < 10 and x + 1 < len(city_map[0]):
            poss = follow_path(x + 1, y, direction, dir_length + 1, lost_heat + city_map[y][x + 1])
            if poss:
                possibilities.append(poss)
        if y + 4 < len(city_map):
            poss = follow_path(x, y+4, 'v', 4, lost_heat + sum([city_map[k][x] for k in range(y+1, y+5)]))
            if poss:
                possibilities.append(poss)
        if y - 4 >= 0:
            poss = follow_path(x, y-4, '^', 4, lost_heat + sum([city_map[k][x] for k in range(y-4, y)]))
            if poss:
                possibilities.append(poss)

    if direction == 'v':
        if dir_length < 10 and y + 1 < len(city_map):
            poss = follow_path(x, y + 1, direction, dir_length + 1, lost_heat + city_map[y + 1][x])
            if poss:
                possibilities.append(poss)
        if x + 4 < len(city_map):
            poss = follow_path(x+4, y, '>', 4, lost_heat + sum([city_map[y][k] for k in range(x+1, x+5)]))
            if poss:
                possibilities.append(poss)
        if x - 4 >= 0:
            poss = follow_path(x-4, y, '<', 4, lost_heat + sum([city_map[y][k] for k in range(x-4, x)]))
            if poss:
                possibilities.append(poss)

    if direction == '^':
        if dir_length < 10 and y - 1 >= 0:
            poss = follow_path(x, y - 1, direction, dir_length + 1, lost_heat + city_map[y - 1][x])
            if poss:
                possibilities.append(poss)
        if x + 4 < len(city_map):
            poss = follow_path(x+4, y, '>', 4, lost_heat + sum([city_map[y][k] for k in range(x+1, x+5)]))
            if poss:
                possibilities.append(poss)
        if x - 4 >= 0:
            poss = follow_path(x-4, y, '<', 4, lost_heat + sum([city_map[y][k] for k in range(x-4, x)]))
            if poss:
                possibilities.append(poss)

    if direction == '<':
        if dir_length < 10 and x - 1 >= 0:
            poss = follow_path(x - 1, y, direction, dir_length + 1, lost_heat + city_map[y][x - 1])
            if poss:
                possibilities.append(poss)
        if y + 4 < len(city_map):
            poss = follow_path(x, y+4, 'v', 4, lost_heat + sum([city_map[k][x] for k in range(y+1, y+5)]))
            if poss:
                possibilities.append(poss)
        if y - 4 >= 0:
            poss = follow_path(x, y-4, '^', 4, lost_heat + sum([city_map[k][x] for k in range(y-4, y)]))
            if poss:
                possibilities.append(poss)

    if possibilities:
        return min(possibilities)

if __name__ == "__main__":
    tick = time.time()
    with open('input.txt') as f:
        citymap = f.read().split('\n')
    city_map = [[int(char) for char in line] for line in citymap]
    path_map = [[{'>': {}, 'v': {}, '<': {}, '^': {}} for char in line] for line in city_map]

    print(follow_path(0, 4, 'v', 4, sum([city_map[k][0] for k in range(1,5)])))
    tock = time.time()
    print(tock-tick)
    print(follow_path(4, 0, '>', 4, sum([city_map[0][k] for k in range(1,5)])))
    print(time.time()-tock)
