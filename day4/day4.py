class Game:
    def __init__(self,game):
        self.winning_numbers = [int(number) for number in game.split(' | ')[0].split(': ')[1].split(' ') if number != '']
        self.numbers = [int(number.strip()) for number in game.split(' | ')[1].split(' ') if number != '']

    def get_score(self):
        score = 0
        for number in self.numbers:
            if number in self.winning_numbers:
                if score < 1:
                    score +=1
                else:
                    score *=2
        return score

    def get_match_count(self):
        matches = 0
        for number in self.numbers:
            if number in self.winning_numbers:
                matches += 1
        return matches


if __name__ == "__main__":
    with open('input.txt') as f:
        games = [Game(game) for game in f.read().split('\n')]
    print(f"Part 1: {sum([game.get_score() for game in games])}")

    counts = [1 for game in games]
    for k in range(len(counts)):
        for j in range(games[k].get_match_count()):
            counts[k+j+1] += counts[k]
    print(f"Part 2: {sum(counts)}")
