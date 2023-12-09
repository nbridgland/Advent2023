import math

if __name__ == "__main__":
    with open('input.txt') as f:
        instructions, lines = f.read().split('\n\n')
    maps = {line.split(' = ')[0]: (line.split(' = ')[1][1:4], line.split(' = ')[1][6:9])
            for line in lines.split('\n')}

    current_pos = 'AAA'
    k = 0
    while current_pos != 'ZZZ':
        if instructions[k % len(instructions)] == 'L':
            current_pos = maps[current_pos][0]
        elif instructions[k % len(instructions)] == 'R':
            current_pos = maps[current_pos][1]
        k += 1
    print(f"Part 1: {k}")

    n_steps = []
    for pos in [pos for pos in maps if pos[2] == 'A']:
        k = 0
        new_pos = pos
        while True:
            if instructions[k % len(instructions)] == 'L':
                new_pos = maps[new_pos][0]
            elif instructions[k % len(instructions)] == 'R':
                new_pos = maps[new_pos][1]
            if new_pos[2] == 'Z':
                n_steps.append(k+1)
                break
            k += 1

    output = 1
    for step in n_steps:
        output = output*step//math.gcd(output, step)
    print(f"Part 2: {output}")
