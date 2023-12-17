def hash_alg(characters):
    current_value = 0
    for char in characters:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


class Boxes:
    def __init__(self):
        self.boxes = [[] for k in range(256)]

    def remove_lens(self, line):
        label = line.split('-')[0]
        box_label = hash_alg(label)
        box = self.boxes[box_label]
        for k in range(len(box)):
            if label in box[k]:
                self.boxes[box_label] = box[:k] + box[k + 1:]

    def add_lens(self, line):
        label, length = line.split('=')
        box_label = hash_alg(label)
        box = self.boxes[box_label]
        for k in range(len(box)):
            if label in box[k]:
                self.boxes[box_label] = box[:k] + [label + ';' + length] + box[k + 1:]
                return None
        self.boxes[box_label].append(label + ';' + length)


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.read().split(',')
    output = 0
    for line in lines:
        output += hash_alg(line)
    print(f"Part 1: {output}")
    boxes = Boxes()
    for line in lines:
        if '-' in line:
            boxes.remove_lens(line)
        if '=' in line:
            boxes.add_lens(line)

    output = 0
    for k in range(len(boxes.boxes)):
        for j in range(len(boxes.boxes[k])):
            output += (k + 1) * (j + 1) * int(boxes.boxes[k][j].split(';')[1])
    print(f"Part 2: {output}")
