numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_number(schematic, row, column):
    adjacent = False
    gears = []
    min_row = max(row-1, 0)
    max_row = min(row+1, len(schematic)-1)
    if column > 0:
        for j in range(min_row, max_row+1):
            if schematic[j][column-1] not in numbers and schematic[j][column-1] != '.':
                adjacent = True
                if schematic[j][column-1] == '*':
                    gears.append((j, column-1))
    number = ''
    while column < len(schematic[row]) and schematic[row][column] in numbers:
        number += schematic[row][column]
        if schematic[min_row][column] not in numbers and schematic[min_row][column] != '.':
            adjacent = True
            if schematic[min_row][column] == '*':
                gears.append((min_row, column))
        if schematic[max_row][column] not in numbers and schematic[max_row][column] != '.':
            adjacent = True
            if schematic[max_row][column] == '*':
                gears.append((max_row, column))
        column += 1
    if not adjacent and column < len(schematic[0]): # really don't need to check if it already is
        for j in range(min_row, max_row+1):
            if schematic[j][column] not in numbers and schematic[j][column] != '.':
                adjacent = True
                if schematic[j][column] == '*':
                    gears.append((j, column))
    return int(number)*adjacent, gears


if __name__ == "__main__":
    with open('input.txt') as f:
        schematic = f.read().split('\n')
    output = 0
    gear_dict = {}
    for k in range(len(schematic)):
        line = schematic[k]
        flag = False
        for j in range(len(line)):
            if line[j] in numbers:
                if not flag:
                    flag = True
                    part_number, gears = get_number(schematic, k, j)
                    if part_number > 0:
                        for gear in gears:
                            if gear not in gear_dict:
                                gear_dict[gear] = [part_number]
                            else:
                                gear_dict[gear].append(part_number)
                        output += part_number
            else:
                flag = False
    print(f"Part 1: {output}")

    output = 0
    for key in gear_dict.keys():
        if len(gear_dict[key]) == 2:
            output += gear_dict[key][0]*gear_dict[key][1]
    print(f"Part 2: {output}")