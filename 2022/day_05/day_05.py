from collections import deque
import re

def part_01(f):
    crates, instructions = f.read().split('\n\n')
    stacks = []

    for line in crates.splitlines():
        for i, pos in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[pos] != " ":
                stacks[i].append(line[pos])

    for instruction in instructions.splitlines():
        n, fs, ts = map(int, re.findall(re.compile(r'\d+'), instruction))
        for c in range(n):
            stacks[ts - 1].appendleft(stacks[fs - 1].popleft())
    return ''.join([s[0] for s in stacks])

def part_02(f):
    crates, instructions = f.read().split('\n\n')
    stacks = []

    for line in crates.splitlines():
        for i, pos in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[pos] != " ":
                stacks[i].append(line[pos])

    for instruction in instructions.splitlines():
        n, fs, ts = map(int, re.findall(re.compile(r'\d+'), instruction))
        crates_to_move = deque()
        for i in range(n):
            crates_to_move.appendleft(stacks[fs - 1].popleft())
        stacks[ts - 1].extendleft(crates_to_move)
    return ''.join([s[0] for s in stacks])

if __name__ == '__main__':
    with open('input.txt') as f:
       print(part_01(f))
    with open('input.txt') as f:
       print(part_02(f))
