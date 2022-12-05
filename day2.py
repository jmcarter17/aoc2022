VALUES = {
    "A X": 4,  # Rock - Rock  (1 + 3 = 4)
    "A Y": 8,  # Rock - Paper (2 + 6 = 8)
    "A Z": 3,  # Rock - Cissors (3 + 0 = 3)
    "B X": 1,  # Paper - Rock  (1 + 0 = 1)
    "B Y": 5,  # Paper - Paper (2 + 3 = 5)
    "B Z": 9,  # Paper - Cissors (3 + 6 = 9)
    "C X": 7,  # Cissors - Rock (1 + 6 = 7)
    "C Y": 2,  # Cissors - Paper (2 + 0 = 2)
    "C Z": 6   # Cissors - Cissors (3 + 3 = 6)
}

RESULTS = {
    "A X": 3,  # Rock - Lose (cissors)  (3 + 0 = 3)
    "A Y": 4,  # Rock - Draw (rock) (1 + 3 = 4)
    "A Z": 8,  # Rock - Win (paper) (2 + 6 = 8)
    "B X": 1,  # Paper - Lose (rock) (1 + 0 = 1)
    "B Y": 5,  # Paper - Draw (paper) (2 + 3 = 5)
    "B Z": 9,  # Paper - Win (cissors) (3 + 6 = 9)
    "C X": 2,  # Cissors - Lose (paper) (2 + 0 = 2)
    "C Y": 6,  # Cissors - Draw (cissors) (3 + 3 = 6)
    "C Z": 7   # Cissors - Win (rock) (1 + 6 = 7)
}


def get_data():
    with open("inputs/day2.txt") as f:
        return [x.strip() for x in f]


def part1(data):
    return sum(VALUES[x] for x in data)


def part2(data):
    return sum(RESULTS[x] for x in data)


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
