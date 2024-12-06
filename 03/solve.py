import re

def parse_input(file_name):
    with open(file_name, 'r') as f:
        content = f.read().strip()
    return content

def get_valid_instructions(riddle):
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)", riddle)

def perform_mul(instruction):
    a, b = re.findall(r"\d{1,3}", instruction)
    return int(a) * int(b)

def perform_all_instructions(riddle):
    instructions = get_valid_instructions(riddle)
    result = 0
    for instruction in instructions:
        result += perform_mul(instruction)
    return result

def delete_dont_instructions(riddle):
    riddle = re.sub(r"don't\(\).+?do\(\)", "", riddle)
    if "don't()" in riddle:
        riddle = riddle.split("don't()")[0]
    return riddle

riddle = parse_input('input.txt')
riddle = riddle.replace('\n', '')
print(perform_all_instructions(riddle))

riddle = delete_dont_instructions(riddle)
print(perform_all_instructions(riddle))