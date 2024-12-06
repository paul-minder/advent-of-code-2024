import numpy as np

def parse_input(file_name):
    with open(file_name, 'r') as f:
        content = f.read().strip().split('\n')
    return [
        np.array(list(map(int, line.split(' '))))
        for line in content
    ]

def goes_in_same_direction(array):
    diffs = np.diff(array)
    return np.all(diffs > 0) or np.all(diffs < 0)

def evolution_within_bounds(array):
    abs_diffs = np.abs(np.diff(array))
    return np.all(abs_diffs <= 3) and np.all(abs_diffs >= 1)

def is_correct(array):
    return goes_in_same_direction(array) and evolution_within_bounds(array)

def is_correct_with_dampener(array):
    if is_correct(array):
        return True
    for i in range(len(array)):
        smaller_array = np.concatenate([array[:i], array[i+1:]])
        if is_correct(smaller_array):
            return True
    return False


# riddle = parse_input('small.txt')
riddle = parse_input('input.txt')

correct_arrays = 0
for i in range(len(riddle)):
    correct_arrays += is_correct(riddle[i])
print(correct_arrays)

correct_arrays_with_dampener = 0
for i in range(len(riddle)):
    correct_arrays_with_dampener += is_correct_with_dampener(riddle[i])
print(correct_arrays_with_dampener)