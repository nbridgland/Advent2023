cube_colors = ['red', 'green', 'blue']
game_conditions = [12, 13, 14]


class Game:
    def __init__(self, game):
        self.index = int(game.split(':')[0].split(' ')[1])
        self.trials = [{color_count.split(' ')[2]: int(color_count.split(' ')[1]) for color_count in trial.split(',')} for trial in game.split(':')[1].split(';')]


if __name__ == "__main__":
    with open('input.txt') as f:
        games = [Game(game) for game in f.read().split('\n')]
    output = 0
    for game in games:
        flag = False
        for trial in game.trials:
            for key in trial:
                if trial[key] > game_conditions[cube_colors.index(key)]:
                    flag = True
        if not flag:
            output += game.index
    print(f"Part 1: {output}")

    output = 0
    for game in games:
        power = 1
        for color in cube_colors:
            for trial in game.trials:
                if color not in trial:
                    trial[color] = 0
            power *= max([trial[color] for trial in game.trials])
        output += power
    print(f"Part 2: {output}")
