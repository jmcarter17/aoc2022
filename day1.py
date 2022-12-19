def get_data():
    with open("inputs/day1.txt") as f:
        all_elves = [[]]
        for x in f:
            x = x.strip()
            if not x:
                all_elves.append([])
            else:
                all_elves[-1].append(int(x))
        return all_elves


def part1(data):
    return max(sum(x) for x in data)


def part2(data):
    return sum(sorted(sum(x) for x in data)[-3:])


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
