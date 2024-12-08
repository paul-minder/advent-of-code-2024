import numpy as np

import cProfile
import pstats
import io

def parse_input(filename):
    with open(filename, 'r') as f:
        content = f.read().strip().split('\n')
    return np.array([list(line) for line in content])

def find_guard(grid):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] in ['^', 'v', '<', '>']:
                return grid[i, j], i, j
    raise ValueError('No guard found')

def compute_next_position(direction, i, j):
    if direction == '^':
        return i - 1, j
    elif direction == 'v':
        return i + 1, j
    elif direction == '<':
        return i, j - 1
    elif direction == '>':
        return i, j + 1
    
def has_guard_left(grid, next_i, next_j):
    if next_i < 0 or next_i >= grid.shape[0]:
        return True
    if next_j < 0 or next_j >= grid.shape[1]:
        return True
    return False

def move_is_valid(grid, i, j):
    return grid[i, j] != '#'

def turn_right(direction):
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'
    elif direction == '<':
        return '^'
    
def is_infinite_loop(grid, guard):
    # allow more than 1 char per cell
    grid = grid.astype('U2')
    direction, i, j = guard
    already_seen = set()
    while True:
        grid[i, j] = 'X'# + direction
        next_i, next_j = compute_next_position(direction, i, j)
        if has_guard_left(grid, next_i, next_j):
            return False
        if move_is_valid(grid, next_i, next_j):
            if (next_i, next_j, direction) in already_seen:
                return True
            else:
                already_seen.add((next_i, next_j, direction))
            grid[next_i, next_j] = direction
            i, j = next_i, next_j

        else:
            direction = turn_right(direction)
            grid[i, j] = 'X'# + direction

def predict_path(grid, guard):
    print_pos = set()
    direction, i, j = guard
    while True:
        print((grid == 'X').sum())
        grid[i, j] = 'X'
        next_i, next_j = compute_next_position(direction, i, j)
        if has_guard_left(grid, next_i, next_j):
            return grid, print_pos
        if move_is_valid(grid, next_i, next_j):
            new_grid = parse_input('input.txt')
            guard = find_guard(new_grid)
            new_grid[next_i, next_j] = '#'
            if is_infinite_loop(new_grid, guard):
                print_pos.add((next_i, next_j))
            grid[next_i, next_j] = direction
            i, j = next_i, next_j
        else:
            direction = turn_right(direction)
            grid[i, j] = direction
            



    
def main():
    filename = 'input.txt'
    grid = parse_input(filename)
    guard = find_guard(grid)
    path, print_pos = predict_path(grid, guard)
    print((path == 'X').sum())
    count = 0
    grid = parse_input(filename)
    for i, j in print_pos:
        if grid[i, j] == '.':
            count += 1
            grid[i, j] = 'O'
    # print grid as str
    for line in grid:
        print(''.join(line))
    print(count)


# Test if putting a obstacle in front create a loop
if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    main()
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())

