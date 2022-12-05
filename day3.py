from more_itertools import grouper


def get_data():
    with open("inputs/day3.txt") as f:
        return [x.strip() for x in f]


def priority_value(elem):
    return ord(elem) - (ord('a') - 1 if ord(elem) >= ord('a') else ord('A') - 27)


def part1(data):
    return sum(priority_value(next(iter(set(x[: len(x) // 2]) & set(x[len(x) // 2 :])))) for x in data)


def part2(data):
    return sum(priority_value(next(iter(set(group[0]) & set(group[1]) & set(group[2])))) for group in grouper(data, 3))


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
