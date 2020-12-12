import math

f = open('Input/12.txt')

instructions = [(string[0], int(string[1:])) for string in f.read().splitlines()]
print(instructions)

pos =[0, 0]
dir = 0

for direction, number in instructions:
    if direction == 'E':
        pos[0] += number
    elif direction == 'W':
        pos[0] -= number
    elif direction == 'N':
        pos[1] += number
    elif direction == 'S':
        pos[1] -= number
    elif direction == 'L':
        dir += number
    elif direction == 'R':
        dir -= number
    elif direction == 'F':
        pos[0] += math.cos(math.radians(dir)) * number
        pos[1] += math.sin(math.radians(dir)) * number
    print(pos, dir)

print(pos, dir)
print("answer:", abs(pos[0]) + abs(pos[1]))
