def race_boat(button_push, total_time):
    return (total_time-button_push)*button_push


if __name__ == "__main__":
    with open('input.txt') as f:
        times, distances = f.read().split('\n')

    times = [int(time) for time in times.split(': ')[1].strip().split('   ')]
    distances = [int(distance) for distance in distances.split(': ')[1].strip().split('  ')]
    output = 1
    for k in range(len(times)):
        button_push = 1
        option_count = 0
        while button_push < times[k]:
            if race_boat(button_push, times[k]) > distances[k]:
                option_count += 1
            button_push += 1
        output *= option_count
    print(f"Part 1: {output}")

    time = int(''.join([str(time) for time in times]))
    distance = int(''.join([str(distance) for distance in distances]))
    button_push = 1
    option_count = 0
    while button_push < time:
        if race_boat(button_push, time) > distance:
            min_push = button_push
            break
        button_push += 1
    button_push = time - 1
    while button_push > 0:
        if race_boat(button_push, time) > distance:
            max_push = button_push
            break
        button_push -= 1
    print(f"Part 2: {max_push - min_push + 1}")
