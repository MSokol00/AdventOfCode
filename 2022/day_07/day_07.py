from pathlib import Path


def part_01(f):
    directories = {}
    p = Path('/')
    for line in f.read().splitlines():
        match line.split():
            case ['$', 'cd', dir]:
                p = p / dir
                p = p.resolve()
            case [size, name] if size.isnumeric():
                for dir in [p, *p.parents]:
                    if dir not in directories:
                        directories[dir] = int(size)
                    else:
                        directories[dir] += int(size)
    return sum(dir_size for dir_size in directories.values() if dir_size <= 100000)


def part_02(f):
    directories = {}
    p = Path('/')
    for line in f.read().splitlines():
        match line.split():
            case ['$', 'cd', dir]:
                p = p / dir
                p = p.resolve()
            case [size, name] if size.isnumeric():
                for dir in [p, *p.parents]:
                    if dir not in directories:
                        directories[dir] = int(size)
                    else:
                        directories[dir] += int(size)
    return min(dir_size for dir_size in directories.values() if directories[Path("/")] - dir_size <= 740000000)


if __name__ == '__main__':
    with open('input.txt') as f:
        print(part_01(f))
    with open('input.txt') as f:
        print(part_02(f))
