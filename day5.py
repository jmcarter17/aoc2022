from copy import deepcopy


def get_data():
    with open("inputs/day5.txt") as f:
        stacks = [[] for _ in range(9)]
        line = next(f)
        while line != "\n":
            for i, c in enumerate(line):
                if c.isalpha():
                    stacks[i // 4].insert(0, c)
            line = next(f)

        actions_gen = (x.split() for x in f)
        actions = [(int(line[1]), int(line[3]), int(line[5])) for line in actions_gen]

        return stacks, actions


def do_action(action, stacks):
    num, src, dest = action
    stacks[dest - 1].extend(reversed(stacks[src - 1][-num:]))
    stacks[src - 1] = stacks[src - 1][0:-num]


def do_action_keep_order(action, stacks):
    num, src, dest = action
    stacks[dest - 1].extend(stacks[src - 1][-num:])
    stacks[src - 1] = stacks[src - 1][0:-num]


def part1(stacks, actions):
    for a in actions:
        do_action(a, stacks)

    return "".join([x[-1] for x in stacks if len(x)])


def part2(stacks, actions):
    for a in actions:
        do_action_keep_order(a, stacks)

    return "".join([x[-1] for x in stacks if len(x)])


def main():
    stacks, actions = get_data()
    print(part1(deepcopy(stacks), actions))
    print(part2(deepcopy(stacks), actions))


if __name__ == "__main__":
    main()
