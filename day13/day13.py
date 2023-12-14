class LavaMap:
    def __init__(self, input_block):
        self.rows = input_block.split('\n')

    def check_horizontal_smudge(self, smudge_tolerance=0):
        for k in range(len(self.rows)):
            size = min(k+1, len(self.rows)-k-1)
            if size == 0:
                break
            smudge_count = 0
            for j in range(size):
                for i in range(len(self.rows[k-j])):
                    if self.rows[k-j][i] != self.rows[k+1+j][i]:
                        smudge_count += 1
                    if smudge_count > smudge_tolerance:
                        break
                if smudge_count > smudge_tolerance:
                    break
            if smudge_count == smudge_tolerance:
                return k

    def check_vertical_smudge(self, smudge_tolerance=0):
        for k in range(len(self.rows[0])):
            size = min(k+1, len(self.rows[0])-k-1)
            if size == 0:
                break
            smudge_count = 0
            for j in range(size):
                for i in range(len(self.rows)):
                    if self.rows[i][k-j] != self.rows[i][k+1+j]:
                        smudge_count += 1
                        if smudge_count > smudge_tolerance:
                            break
                if smudge_count > smudge_tolerance:
                    break
            if smudge_count == smudge_tolerance:
                return k


def score(lava_maps, smudge_tolerance):
    output = 0
    for lava_map in lava_maps:
        hor = lava_map.check_horizontal_smudge(smudge_tolerance)
        if hor is not None:
            output += 100*(hor+1)
        else:
            output += lava_map.check_vertical_smudge(smudge_tolerance) + 1
    return output


if __name__ == "__main__":
    with open('input.txt') as f:
        maps = [LavaMap(section) for section in f.read().split('\n\n')]
    print(f"Part 1: {score(maps, 0)}")
    print(f"Part 2: {score(maps, 1)}")
