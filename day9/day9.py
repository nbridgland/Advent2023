class Predictor:
    def __init__(self, history):
        self.history = [int(number) for number in history.split(' ')]

    def predict(self):
        output = self.history[-1]
        differences = self.history
        while set(differences) != {0}:
            differences = [differences[k+1] - differences[k] for k in range(len(differences)-1)]
            output += differences[-1]
        return output

    def extrapolate_backwards(self):
        output = self.history[0]
        differences = self.history
        counter = 0
        while set(differences) != {0}:
            differences = [differences[k+1] - differences[k] for k in range(len(differences)-1)]
            output = differences[0] - output
            counter += 1
        return (-1)**counter*output


if __name__ == "__main__":
    with open('input.txt') as f:
        histories = [Predictor(line) for line in f.read().split('\n')]
        print(f"Part 1: {sum([predictor.predict() for predictor in histories])}")
        for predictor in histories:
            print(predictor.extrapolate_backwards())
        print(f"Part 2: {sum([predictor.extrapolate_backwards() for predictor in histories])}")
