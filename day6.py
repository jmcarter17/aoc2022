def get_data():
    with open("inputs/day6.txt") as f:
        return f.read().strip()


def find_non_repeating(string, num):
    for i in range(len(string) - num):
        if len(set(string[i:i+num])) == num:
            return i + num


def part1(data):
    return find_non_repeating(data, 4)


def part2(data):
    return find_non_repeating(data, 14)


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
