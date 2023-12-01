def find_marker(input, num_of_unique):
    for i in range(num_of_unique, len(input)):
        if len(set(input[i-num_of_unique:i])) == num_of_unique:
            return i

def part_01(input):
    return find_marker(input, 4)

def part_02(input):
    return find_marker(input, 14)


if __name__ == '__main__':
    with open('input.txt') as f:
        print(part_01(f.read()))
    with open('input.txt') as f:
        print(part_02(f.read()))