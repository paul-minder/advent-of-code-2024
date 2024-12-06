import numpy as np

WORD = "XMAS"

def parse_input(file_name):
    with open(file_name, 'r') as f:
        content = f.read().strip().split('\n')
    return np.array([list(x) for x in content])

def count_occurences(chars, occurence):
    line = "".join(chars)
    return line.count(occurence) + line[::-1].count(occurence)

def iter_matrix_diags(matrix):
    for i in range(-matrix.shape[0]+1, matrix.shape[1]):
        yield matrix.diagonal(i)

def search_xmas(matrix):
    count = 0
    for row in matrix:
        count += count_occurences(row, WORD)
    for col in matrix.T:
        count += count_occurences(col, WORD)
    for diag in iter_matrix_diags(matrix):
        count += count_occurences(diag, WORD)
    for diag in iter_matrix_diags(np.fliplr(matrix)):
        count += count_occurences(diag, WORD)
    return count

def is_x_max(matrix):
    return (count_occurences(matrix.diagonal(), "MAS") == 1) and (count_occurences(np.fliplr(matrix).diagonal(), "MAS") == 1)

def search_x_mas(riddle):
    d = 3
    count = 0
    for i in range(riddle.shape[0]-d+1):
        for j in range(riddle.shape[1]-d+1):
            count += is_x_max(riddle[i:i+d, j:j+d])
    return count

file_name = 'input.txt'
riddle = parse_input(file_name)

print(search_xmas(riddle))
print(search_x_mas(riddle))

# matrix = np.array(
#     [
#         ['A', 'B', 'C', 'D'],
#         ['E', 'F', 'G', 'H'],
#         ['I', 'J', 'K', 'L'],
#     ]
# )

# print(matrix)
# for diag in iter_matrix_diags(matrix):
#     print(diag)
# print(np.fliplr(matrix))
# for diag in iter_matrix_diags(np.fliplr(matrix)):
#     print(diag)