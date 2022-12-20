import numpy as np


def get_data():
    with open("inputs/day8.txt") as f:
        return np.array([[int(d) for d in x.strip()] for x in f])


def part1(data):
    w, h = data.shape
    visible = np.zeros_like(data)

    for row in range(w):
        for col in range(h):
            if row == 0 or row == w - 1 or col == 0 or col == h - 1:
                visible[row, col] = 1
            elif any((
                np.all(data[row, :][:col] < data[row, col]),
                np.all(data[row, :][col + 1 :] < data[row, col]),
                np.all(data[:, col][:row] < data[row, col]),
                np.all(data[:, col][row + 1 :] < data[row, col]),
            )):
                visible[row, col] = 1

    return np.sum(visible)


def view_distance(val, arr):
    for i, v in enumerate(arr):
        if v >= val:
            return i + 1

    return len(arr)

    # print(val, arr, test)


def scenic_score(data, row, col):
    up = data[row, :][:col][::-1]
    down = data[row, :][col+1:]
    left = data[:, col][:row][::-1]
    right = data[:, col][row+1:]

    scores = []
    for arr in (up, down, left, right):
        scores.append(view_distance(data[row, col], arr))

    return np.prod(scores)


def part2(data):
    w, h = data.shape
    scores = []
    for row in range(1, w-1):
        for col in range(1, h-1):
            scores.append(scenic_score(data, row, col))
    return max(scores)


def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
