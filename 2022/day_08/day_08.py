def check_if_visible(x, y, t_map):
    tree_height = t_map[y][x]
    # check horizontal left
    if all(tree < tree_height for tree in t_map[y][:x]):
        return True
    # check horizontal right
    if all(tree < tree_height for tree in t_map[y][x + 1:]):
        return True
    # check vertical up
    if all(tree < tree_height for tree in [row[x] for row in t_map[:y]]):
        return True
    # check vertical down
    if all(tree < tree_height for tree in [row[x] for row in t_map[y + 1:]]):
        return True


def part_01(f_obj):
    map_of_trees = [list(map(int, line)) for line in f_obj.read().splitlines()]
    visible = (len(map_of_trees) - 1) * 4
    for y in range(1, len(map_of_trees) - 1):
        for x in range(1, len(map_of_trees) - 1):
            if check_if_visible(x, y, map_of_trees):
                visible += 1
    return visible


def calculate_scenic_score(x, y, t_map):
    left = 0
    right = 0
    up = 0
    down = 0
    tree_height = t_map[y][x]
    # check horizontal left
    for tree in reversed(t_map[y][:x]):
        left += 1
        if tree >= tree_height:
            break
    # check horizontal right
    for tree in t_map[y][x + 1:]:
        right += 1
        if tree >= tree_height:
            break
    # check vertical up
    for tree in [row[x] for row in reversed(t_map[:y])]:
        up += 1
        if tree >= tree_height:
            break
    # check vertical down
    for tree in [row[x] for row in t_map[y + 1:]]:
        down += 1
        if tree >= tree_height:
            break
    return left * right * up * down


def part_02(f_obj):
    map_of_trees = [list(map(int, line)) for line in f_obj.read().splitlines()]
    scenic_scores = []
    for y in range(len(map_of_trees)):
        for x in range(len(map_of_trees)):
            scenic_scores.append(calculate_scenic_score(x, y, map_of_trees))
    return max(scenic_scores)


if __name__ == '__main__':
    with open('input.txt') as f:
        print(part_01(f))
    with open('input.txt') as f:
        print(part_02(f))
