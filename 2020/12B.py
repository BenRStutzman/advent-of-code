import math

f = open('Input/12.txt')

instructions = [(string[0], int(string[1:])) for string in f.read().splitlines()]

waypoint_pos = [10, 1]
pos = [0, 0]

def rotate(waypoint_pos, angle):
    radius = math.sqrt(waypoint_pos[0] ** 2 + waypoint_pos[1] ** 2)
    dir = math.atan2(waypoint_pos[1], waypoint_pos[0])
    dir += math.radians(angle)
    return [math.cos(dir) * radius, math.sin(dir) * radius]

for direction, number in instructions:
    if direction == 'E':
        waypoint_pos[0] += number
    elif direction == 'W':
        waypoint_pos[0] -= number
    elif direction == 'N':
        waypoint_pos[1] += number
    elif direction == 'S':
        waypoint_pos[1] -= number
    elif direction == 'L':
        waypoint_pos = rotate(waypoint_pos, number)
    elif direction == 'R':
        waypoint_pos = rotate(waypoint_pos, -number)
    elif direction == 'F':
        pos[0] += waypoint_pos[0] * number
        pos[1] += waypoint_pos[1] * number
    print(pos, waypoint_pos)

print("answer:", abs(pos[0]) + abs(pos[1]))
