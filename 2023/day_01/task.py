import re

mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return int(mapping[value])

def part_01(f):
    res_sum = 0
    pattern = re.compile(r'\d')
    for line in f.read().splitlines():
        if match := pattern.findall(line):
            res_sum += int(f'{match[0]}{match[-1]}')
    return res_sum

def part_02(f):
    res_sum = 0
    pattern = re.compile(f'(?=(\\d|{"|".join(mapping.keys())}))')
    for line in f.read().splitlines():
        if match := pattern.findall(line):
            res_sum += int(f'{convert_to_int(match[0])}{convert_to_int(match[-1])}')
    return res_sum


if __name__ == '__main__':
    with open('input.txt') as f:
        print(part_01(f))
    with open('input.txt') as f:
        print(part_02(f))
