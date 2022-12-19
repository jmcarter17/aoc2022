from functools import lru_cache


def get_data():
    with open("inputs/day7.txt") as f:
        commands = []
        for c in f:
            cmd = c.replace("$ ", "").strip()
            if cmd[0:4] != "ls" and cmd[0:3] != "dir":
                commands.append(cmd.split())
        return commands


class FilesysObj:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    @property
    def size(self):
        raise NotImplementedError

    def __repr__(self):
        return f"{type(self).__name__}({self.name})"


class File(FilesysObj):
    def __init__(self, name, size, parent):
        super().__init__(name, parent)
        self._size = size

    @property
    def size(self):
        return self._size


class Dir(FilesysObj):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.children = []

    @property
    @lru_cache(maxsize=None)
    def size(self):
        return sum(child.size for child in self.children)

    def add_child(self, child):
        self.children.append(child)


def run_command(folder, cmd):
    if cmd[0] != "cd":
        folder.add_child(File(cmd[1], int(cmd[0]), folder))
    elif cmd[1] == "..":
        folder = folder.parent
    elif cmd[1] != "/":
        child = Dir(cmd[1], folder)
        folder.add_child(child)
        folder = child

    return folder


def get_size_dirs(sizes, filesys):
    sizes.append(filesys.size)
    for c in filesys.children:
        if isinstance(c, Dir):
            get_size_dirs(sizes, c)
    

def part1_and_2(data):
    filesys = Dir("/", None)
    folder = filesys
    for cmd in data:
        folder = run_command(folder, cmd)

    sizes = []
    get_size_dirs(sizes, filesys)

    part1_answer = sum(x for x in sizes if x <= 100000)
    print("Part 1:", part1_answer)

    # Part 2
    unused = 70000000 - filesys.size
    needed = 30000000 - unused
    part2_answer = min(s for s in sizes if s >= needed)
    print("Part 2:", part2_answer)


def part1_and_2_stackbased(data):
    sizes = {}
    stack = []

    for i, cmd in enumerate(data):
        if cmd[0] == "cd":
            folder = cmd[1]
            if folder == "..":
                stack.pop()
            else:
                stack.append(i)
                sizes[i] = 0
        else:
            size = int(cmd[0])
            for s in stack:
                sizes[s] += size

    part1_answer = sum(size for size in sizes.values() if size <= 100000)
    print("Part 1 answer:", part1_answer)

    # Part 2
    unused = 70000000 - sizes[0]
    needed = 30000000 - unused
    part2_answer = min(s for s in sizes.values() if s >= needed)
    print("Part 2 answer:", part2_answer)


def main():
    data = get_data()
    part1_and_2(data)
    part1_and_2_stackbased(data)


if __name__ == "__main__":
    main()
