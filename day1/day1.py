numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spelled_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def find_calibration_value(line):
    for char1 in line:
        if char1 in numbers:
            break
    if char1 not in numbers:
        return 0
    for char2 in line[::-1]:
        if char2 in numbers:
            break
    if char2 not in numbers:
        return 0
    return int(char1+char2)


def find_all_instances(line, number):
    number_indicies = []
    number_index = line.find(number)
    last_number_index = -1
    while number_index != last_number_index:
        number_indicies.append(number_index)
        last_number_index = number_index
        number_index += 1 + line[number_index+1:].find(number)
    return number_indicies


def alt_find_calibration_value(line):
    locations = {}
    for k in range(len(line)):
        if line[k] in numbers:
            locations[k] = line[k]
    for k in range(len(spelled_numbers)):
        number_index = line.find(spelled_numbers[k])
        if number_index > -1:
            number_indicies = find_all_instances(line, spelled_numbers[k])
            for number_index in number_indicies:
                locations[number_index] = str(k)
    return int(locations[min(locations.keys())] + locations[max(locations.keys())])


if __name__ == "__main__":
    with open('input.txt') as f:
        data = f.read()

    lines = data.split('\n')
    print(f"Part 1: {sum([find_calibration_value(line) for line in lines])}")
    print(f"Part 2: {sum([alt_find_calibration_value(line) for line in lines])}")
