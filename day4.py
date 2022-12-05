def get_data():
    with open("inputs/day4.txt") as f:
        pairs = []
        for x in f:
            x = x.strip()
            (r1l, r1h, r2l, r2h) = (int(v) for y in x.split(",") for v in y.split("-"))
            pairs.append((range(r1l, r1h + 1), range(r2l, r2h + 1)))
        return pairs


def is_contained(rng1, rng2):
    return (rng1.start >= rng2.start and rng1.stop <= rng2.stop) or (
        rng2.start >= rng1.start and rng2.stop <= rng1.stop
    )


def intersects(rng1, rng2):
    return rng1.start < rng2.stop and rng1.stop > rng2.start


def part1(data):
    return sum(is_contained(rng1, rng2) for rng1, rng2 in data)


def part2(data):
    return sum(intersects(rng1, rng2) for rng1, rng2 in data)


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
