f = open('Input/8.txt')

split_lines = [line.split() for line in f.read().splitlines()]
instructions = [[line[0], int(line[1])] for line in split_lines]
instructions.append(("stp", 0))

def execute(instructions):
    acc = 0
    next_line = 0
    visited_lines = []

    while next_line not in visited_lines:
        visited_lines.append(next_line)
        instruction, number = instructions[next_line]
        if instruction == "stp":
            return acc
        if instruction == "acc":
            acc += number
        if instruction == "jmp":
            next_line += number
        else:
            next_line += 1

    return False

def switch_instruction(instruction):
    if instruction == "jmp":
        return "nop"
    else:
        return "jmp"

switchers = ["jmp", "nop"]

for index, [instruction, number] in enumerate(instructions):
    if instruction in switchers:
        instructions[index][0] = switch_instruction(instruction)
        acc = execute(instructions)
        if acc:
            print(index)
            break
        instructions[index][0] = instruction


print("answer:", acc)
