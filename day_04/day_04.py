def part_01():
    with open('input.txt') as f:
        number_of_overlapping = 0
        for line in f:
            line = line.strip('\n')
            e1s, e1e = map(int, line.split(',')[0].split('-'))
            e2s, e2e = map(int, line.split(',')[1].split('-'))
            e1 = set(range(e1s, e1e + 1))
            e2 = set(range(e2s, e2e + 1))
            intersection = e1 & e2
            if intersection == e1 or intersection == e2:
                number_of_overlapping += 1
    return number_of_overlapping

def part_02():
    with open('input.txt') as f:
        number_of_overlapping = 0
        for line in f:
            line = line.strip('\n')
            e1s, e1e = map(int, line.split(',')[0].split('-'))
            e2s, e2e = map(int, line.split(',')[1].split('-'))
            e1 = set(range(e1s, e1e + 1))
            e2 = set(range(e2s, e2e + 1))
            if e1 & e2:
                number_of_overlapping +=1
    return number_of_overlapping

if __name__ == '__main__':
    print(part_01())
    print(part_02())
