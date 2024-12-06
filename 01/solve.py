import numpy as np
from collections import Counter

def parse_file(file_name):
    with open(file_name, 'r') as f:
        content = f.read().strip().split('\n')
    a, b = [], []
    for line in content:
        x, y = line.split('   ')
        a.append(int(x))
        b.append(int(y))
    return np.array(a), np.array(b)

def solve_first_part(a, b):
    a.sort()
    b.sort()
    return np.abs(a - b).sum()

def solve_second_part(a, b):
    numbers_in_a = set(a)
    occurences_in_b = Counter(b)
    similarity = 0
    for number in a:
        if number in occurences_in_b:
            similarity += occurences_in_b[number] * number
    return similarity
        

file_path = 'input.txt'
# file_path = 'small.txt'
a, b = parse_file(file_path)
print(solve_first_part(a, b))
print(solve_second_part(a, b))


