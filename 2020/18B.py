f = open('Input/18.txt')

lines = []

for line in f.read().splitlines():
    this_line = []
    for word in line.split(' '):
        start_parens = word.count('(')
        end_parens = word.count(')')
        for i in range(start_parens):
            this_line.append('(')
        end_index = -end_parens if end_parens else len(word)
        this_line.append(word[start_parens:end_index])
        for i in range(end_parens):
            this_line.append(')')
    lines.append(this_line)

def multiply_things(total, things_to_multiply):
    for thing_to_multiply in things_to_multiply:
        total *= thing_to_multiply
    return total

def evaluate(line):
    i = 0
    total = None
    things_to_multiply = []
    while i < len(line):
        char = line[i]
        i += 1

        if char == '+':
            continue
        elif char == '*':
            things_to_multiply.append(total)
            total = None
            continue
        elif char == ')':
            break
        elif char == '(':
            next_val, skip = evaluate(line[i:])
            i += skip
        else:
            next_val = int(char)

        if total is None:
            total = next_val
        else:
            total += next_val
    return multiply_things(total, things_to_multiply), i

total = 0

for line in lines:
    result = evaluate(line)[0]
    print(result)
    total += result

print("answer:", total)
