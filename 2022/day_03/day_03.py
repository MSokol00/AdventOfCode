PRIORITY = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def part_01():
    with open('input.txt') as f:
        duplicates = []
        for line in f:
            line = line.strip('\n')
            p1, p2 = line[0:int(len(line) / 2)], line[int(len(line) / 2):]
            duplicates.extend({i for i in p1 if i in p2})
        return sum(map(lambda l: PRIORITY.index(l) + 1, duplicates))


def part_02():
    with open('input.txt') as f:
        i = 0
        badges = []
        rucksacks = []
        for line in f:
            line = line.strip('\n')
            rucksacks.append(line)
            i += 1
            if i == 3:
                badges.extend({i for i in rucksacks[0] if i in {n for n in rucksacks[1] if n in rucksacks[2]}})
                i = 0
                rucksacks = []
        return sum(map(lambda l: PRIORITY.index(l) + 1, badges))


if __name__ == '__main__':
    print(part_01())
    print(part_02())
