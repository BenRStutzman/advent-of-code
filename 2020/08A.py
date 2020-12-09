f = open('Input/8.txt')

split_lines = [line.split() for line in f.read().splitlines()]
instructions = [(line[0], int(line[1])) for line in split_lines]

acc = 0
next_line = 0
visited_lines = []

while next_line not in visited_lines:
    visited_lines.append(next_line)
    instruction, number = instructions[next_line]
    if instruction == "acc":
        acc += number
    if instruction == "jmp":
        next_line += number
    else:
        next_line += 1

print("answer:", acc)
