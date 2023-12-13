import time

string_dict = {}


class SpringCollection:
    def __init__(self, input_line):
        self.springs = input_line.split(' ')[0]
        self.groups = [int(number) for number in input_line.split(' ')[1].split(',')]


def preprocess_string(string):
    output_string = ''
    k = 0
    while k < len(string):
        if string[k] != '.':
            output_string = output_string + string[k]
            k += 1
        else:
            if k != 0:
                output_string = output_string + string[k]
            while string[k] == '.':
                if k == len(string) - 1:
                    output_string = output_string[:len(output_string) - 1]
                    return output_string
                k += 1
    return output_string


def process_string(string, groups):
    if len(groups) == 0:
        if '#' not in string:
            return 1
        else:
            return 0
    if string in string_dict:
        if str(groups) in string_dict[string]:
            return string_dict[string][str(groups)]
        else:
            string_dict[string][str(groups)] = 0
    else:
        string_dict[string] = {}
        string_dict[string][str(groups)] = 0

    j = 0
    broken = False
    while j < len(string) and string[j] != '.':
        if string[j] == '#':
            broken = True
        j += 1
    if j < groups[0]:
        if broken:
            string_dict[string][str(groups)] = 0
            return 0
    elif j == groups[0]:
        new_string = string[j + 1:]
        new_groups = groups[1:]
        string_dict[string][str(groups)] += process_string(new_string, new_groups)
    else:
        if string[groups[0]] != '#':
            string_dict[string][str(groups)] += process_string(string[groups[0] + 1:], groups[1:])
        k = 0
        while string[k] == '?' and k + groups[0] + 1 < j:
            if string[k + groups[0] + 1] == '?':
                string_dict[string][str(groups)] += process_string(string[k + groups[0] + 2:], groups[1:])
            k += 1
        if string[k] == '?':
            string_dict[string][str(groups)] += process_string(string[j + 1:], groups[1:])
    if not broken:
        new_string = string[j + 1:]
        string_dict[string][str(groups)] += process_string(new_string, groups)
    return string_dict[string][str(groups)]


if __name__ == "__main__":
    tick = time.time()
    with open('input.txt') as f:
        records = [SpringCollection(line) for line in f.read().split('\n')]
    output = 0
    for record in records:
        string = preprocess_string(record.springs)
        groups = record.groups
        output += process_string(string, groups)
    print(f"Part 1: {output}")
    tock = time.time()

    print(tock - tick, '\n')

    # Part 2
    output = 0
    for record in records:
        record.springs = '?'.join([record.springs for k in range(5)])
        record.groups = record.groups * 5
        string = preprocess_string(record.springs)
        groups = record.groups
        output += process_string(string, groups)
    print(f'Part 2: {output}')
    print(time.time() - tock)
