class Dish:
    def __init__(self, dish_map):
        self.dish = dish_map

    def tilt_north(self):
        new_map = ['' for row in self.dish]
        for j in range(len(self.dish[0])):
            col = ''
            for k in range(len(self.dish)):
                if self.dish[k][j] == '#':
                    while len(col) < k:
                        col += '.'
                    col += '#'
                if self.dish[k][j] == 'O':
                    col += 'O'
            while len(col) < len(self.dish):
                col += '.'
            for i in range(len(new_map)):
                new_map[i] += col[i]
        self.dish = new_map

    def tilt_west(self):
        new_map = ['' for row in self.dish]
        for k in range(len(self.dish)):
            row = ''
            for j in range(len(self.dish[0])):
                if self.dish[k][j] == '#':
                    while len(row) < j:
                        row += '.'
                    row += '#'
                if self.dish[k][j] == 'O':
                    row += 'O'
            while len(row) < len(self.dish[0]):
                row += '.'
            new_map[k] = row
        self.dish = new_map

    def tilt_south(self):
        new_map = ['' for row in self.dish]
        for j in range(len(self.dish[0])):
            col = ''
            for k in range(len(self.dish))[::-1]:
                if self.dish[k][j] == '#':
                    while len(col) < (len(self.dish) - 1 - k):
                        col += '.'
                    col += '#'
                if self.dish[k][j] == 'O':
                    col += 'O'
            while len(col) < len(self.dish):
                col += '.'
            for i in range(len(new_map)):
                new_map[i] += col[::-1][i]
        self.dish = new_map

    def tilt_east(self):
        new_map = ['' for row in self.dish]
        for k in range(len(self.dish)):
            row = ''
            for j in range(len(self.dish[0]))[::-1]:
                if self.dish[k][j] == '#':
                    while len(row) < (len(self.dish[0]) - 1 - j):
                        row += '.'
                    row += '#'
                if self.dish[k][j] == 'O':
                    row += 'O'
            while len(row) < len(self.dish[0]):
                row += '.'
            new_map[k] = row[::-1]
        self.dish = new_map

    def get_load(self):
        output = 0
        for k in range(len(self.dish)):
            for char in self.dish[k]:
                if char == 'O':
                    output += len(self.dish) - k
        return output


if __name__ == "__main__":
    with open('input.txt') as f:
        tilt_dish = Dish(f.read().split('\n'))
    tilt_dish.tilt_north()
    print(f"Part 1: {tilt_dish.get_load()}")
    seen = []
    tilt_dish.tilt_west()
    tilt_dish.tilt_south()
    tilt_dish.tilt_east()
    while tilt_dish.dish not in seen:
        seen.append(tilt_dish.dish)
        tilt_dish.tilt_north()
        tilt_dish.tilt_west()
        tilt_dish.tilt_south()
        tilt_dish.tilt_east()
    cycle_length = len(seen) - seen.index(tilt_dish.dish)
    n_rotations = 1 + len(seen)
    remaining_rotations = (1000000000 - n_rotations) % cycle_length
    for rotation in range(remaining_rotations):
        tilt_dish.tilt_north()
        tilt_dish.tilt_west()
        tilt_dish.tilt_south()
        tilt_dish.tilt_east()
    print(f"Part 2: {tilt_dish.get_load()}")
