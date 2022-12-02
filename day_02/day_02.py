F_MAP = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}
F_MAP_WIN = {
    'ROCK': {
        'PAPER': 'PAPER',
        'SCISSORS': 'ROCK'
    },
    'PAPER': {
        'ROCK': 'PAPER',
        'SCISSORS': 'SCISSORS'
    },
    'SCISSORS': {
        'ROCK': 'ROCK',
        'PAPER': 'SCISSORS'
    }
}
FIGURE_POINTS = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}
GAME_MAP = {
    'X': 'LOSE',
    'Y': 'DRAW',
    'Z': 'WIN'
}
F_MAP_GAME = {
    'ROCK': {
        'LOSE': 'SCISSORS',
        'WIN': 'PAPER'
    },
    'PAPER': {
        'LOSE': 'ROCK',
        'WIN': 'SCISSORS'
    },
    'SCISSORS': {
        'LOSE': 'PAPER',
        'WIN': 'ROCK'
    }
}
GAME_POINTS = {
    'WIN': 6,
    'LOSE': 0,
    'DRAW': 3
}

def part_01():
    total_points = 0
    with open('input.txt') as file:
        for line in file:
            line = line.strip('\n')
            opponent, me = line.split(' ')
            total_points += FIGURE_POINTS.get(F_MAP.get(me)) + _game_points(opponent, me)
    return total_points

def _game_points(opponent, me):
    opponent = F_MAP.get(opponent)
    me = F_MAP.get(me)
    if opponent == me:
        return 3
    win = F_MAP_WIN[opponent][me]
    if win == me:
        return 6
    return 0

############## PART 2 ##############

def part_02():
    total_points = 0
    with open('input.txt') as file:
        for line in file:
            line = line.strip('\n')
            opponent, output = line.split(' ')
            me = F_MAP_GAME.get(opponent := F_MAP.get(opponent)).get(output := GAME_MAP.get(output))
            if output == 'DRAW':
                total_points += 3 + FIGURE_POINTS.get(opponent)
            if output == 'LOSE':
                total_points += FIGURE_POINTS.get(me)
            if output == 'WIN':
                total_points += 6 + FIGURE_POINTS.get(me)
    return total_points




if __name__ == '__main__':
    print(part_02())