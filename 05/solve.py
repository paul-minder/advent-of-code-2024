def parse_input(file_name):
    with open(file_name, 'r') as f:
        rules, cases = f.read().strip().split('\n\n')
    return rules.split('\n'), cases.split('\n')

def parse_rules(rules):
    d = {}
    for rule in rules:
        k, v = rule.split('|')
        d[k] = d.get(k, []) + [v]
    return d

def parse_case(case):
    return case.split(',')

def case_follow_rules(case, rules):
    case = parse_case(case)
    case = case[::-1]
    for i in range(len(case) - 1):
        k = case[i]
        if k not in rules:
            continue
        for j in range(i, len(case)):
            if case[j] in rules[k]:
                return False
    return True

def get_middle_page(case):
    case = parse_case(case)
    if len(case) % 2 == 0:
        raise ValueError('Case must have odd number of pages')
    return int(case[len(case) // 2])

def add_element_in_case(ordered_case, element, rules):
    for i in range(len(ordered_case)+1):
        test = ordered_case[:i] + [element] + ordered_case[i:]
        test = ",".join(test)
        if case_follow_rules(test, rules):
            # print("element added")
            # print(test)
            # print()
            return test.split(',')
    raise ValueError('No place to add element')
        

def put_case_in_order(case, rules):
    case = parse_case(case)
    ordered_case = [case[0]]
    for i in range(1, len(case)):
        ordered_case = add_element_in_case(ordered_case, case[i], rules)
    return ",".join(ordered_case)





rules, cases = parse_input('input.txt')
rules = parse_rules(rules)
count = 0
for case in cases:
    if case_follow_rules(case, rules):
        count += get_middle_page(case)
print(count)

count = 0
for case in cases:
    if not case_follow_rules(case, rules):
        ordered_case = put_case_in_order(case, rules)
        count += get_middle_page(ordered_case)
print(count)


