class Map:
    def __init__(self, lines):
        self.sources = []
        self.destinations = []
        for line in lines.split('\n')[1:]:
            numbers = [int(number) for number in line.split(' ')]
            self.sources.append((numbers[1], numbers[1] + numbers[2]))
            self.destinations.append((numbers[0], numbers[0] + numbers[2]))

    def get_destination(self, source):
        for k in range(len(self.sources)):
            if self.sources[k][0] <= source < self.sources[k][1]:
                return self.destinations[k][0] + (source - self.sources[k][0])
        return source

    def get_source(self, destination):
        for k in range(len(self.destinations)):
            if self.destinations[k][0] <= destination < self.destinations[k][1]:
                return self.sources[k][0] + (destination - self.destinations[k][0])
        if self.get_destination(destination) == destination:
            return destination
        else:
            return None


class BuildMap:
    def __init__(self):
        self.sources = []
        self.destinations = []


def follow_seed(seed, maps):
    for map in maps:
        seed = map.get_destination(seed)
    return seed


def retrace_seed(location, maps):
    for map in maps[::-1]:
        if location:
            location = map.get_source(location)
        else:
            return None
    return location


if __name__ == "__main__":
    with open('input.txt') as f:
        contents = f.read().split('\n\n')

    seeds = [int(number) for number in contents[0].split(': ')[1].split(' ')]
    maps = [Map(map) for map in contents[1:]]

    print(f"Part 1: {min([follow_seed(seed, maps) for seed in seeds])}")
    k = 0
    found = False
    while not found:
        seed = retrace_seed(k, maps)
        if seed:
            for j in range(len(seeds) // 2):
                if seeds[2 * j] <= seed < (seeds[2 * j] + seeds[2 * j + 1]):
                    print(f"Part 2: {k}")
                    found = True
        k += 1
