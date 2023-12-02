import re


def part_01(f, red: int, green: int, blue: int) -> int:
    line_pattern = re.compile(r'Game (?P<game>\d+):\s(?P<sets>.*)')
    balls_pattern = re.compile(r'(\d+) (red|green|blue)')


    result = 0
    for line in f.read().splitlines():
        game = line_pattern.search(line)
        game_possible = True
        for balls_set in game.group('sets').split(';'):
            for ball in balls_set.split(','):
                ball_number = int(balls_pattern.search(ball).groups()[0])
                if (
                        'red' in ball and ball_number > red
                        or 'green' in ball and ball_number > green
                        or 'blue' in ball and ball_number > blue
                ):
                    game_possible = False
            if not game_possible:
                continue
        if game_possible:
            result += int(game.group('game'))
    return result


def part_02(f):
    line_pattern = re.compile(r'Game (?P<game>\d+):\s(?P<sets>.*)')
    balls_pattern = re.compile(r'(\d+) (red|green|blue)')
    result = 0

    for line in f.read().splitlines():
        game = line_pattern.search(line)
        red_balls = 0
        green_balls = 0
        blue_balls = 0
        for balls_set in game.group('sets').split(';'):
            for ball in balls_set.split(','):
                ball_number = int(balls_pattern.search(ball).groups()[0])
                if 'red' in ball and ball_number > red_balls:
                    red_balls = ball_number
                if 'green' in ball and ball_number > green_balls:
                    green_balls = ball_number
                if 'blue' in ball and ball_number > blue_balls:
                    blue_balls = ball_number
        result += red_balls * green_balls * blue_balls
    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        print(part_01(f, 12, 13, 14))
    with open('input.txt') as f:
        print(part_02(f))
