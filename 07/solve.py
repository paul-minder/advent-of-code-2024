def parse_input(file_name):
    with open(file_name, 'r') as f:
        content = f.read().strip().split('\n')
    return [
        parse_line(line) for line in content
    ]

def parse_line(line):
    line = line.split(':')
    result = int(line[0])
    equation_members = line[1].strip().split(' ')
    equation_members = [int(member) for member in equation_members]
    return result, equation_members


def is_solvable(result, equation_members):
    if len(equation_members) == 1:
        return result == equation_members[0]
    if result < 0:
        return False
    if len(str(result)) == 0:
        return True
    output = False
    result_end = str(result)[-len(str(equation_members[-1])):]
    if result_end == str(equation_members[-1]) and len(str(result)) > len(str(equation_members[-1])):
        output = output or is_solvable(
            int(str(result)[:-len(str(equation_members[-1]))]),
            equation_members[:-1]
        )
    if result % equation_members[-1] == 0:
        output = output or is_solvable(
            result // equation_members[-1], equation_members[:-1]
        )
    output = output or is_solvable(
        result - equation_members[-1], equation_members[:-1]
    )
    return output


equations = parse_input('input.txt')
total = 0
for equation in equations:
    result, members = equation
    # print(equation)
    # print(is_solvable(result, members))
    if is_solvable(result, members):
        total += result
print(total)
