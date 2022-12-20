import numpy as np
from math import prod


def get_data():
    with open("inputs/day8.txt") as f:
        return np.array([[int(d) for d in x.strip()] for x in f])


def get_all_directions(data, row, col):
    return data[row, :][:col][::-1], data[row, :][col + 1 :], data[:, col][:row][::-1], data[:, col][row + 1 :]


def part1(data):
    w, h = data.shape
    visible = np.ones_like(data)

    for row in range(1, w - 1):
        for col in range(1, h - 1):
            if all(np.any(arr >= data[row, col]) for arr in get_all_directions(data, row, col)):
                visible[row, col] = 0

    return np.sum(visible)


def view_distance(val, arr):
    for i, v in enumerate(arr, 1):
        if v >= val:
            return i

    return len(arr)


def scenic_score(data, row, col):
    return prod(view_distance(data[row, col], arr) for arr in get_all_directions(data, row, col))


def part2(data):
    w, h = data.shape
    return max(scenic_score(data, row, col) for row in range(1, w - 1) for col in range(1, h - 1))


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
