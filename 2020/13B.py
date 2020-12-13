import math
f = open('Input/13.txt')

lines = f.read().splitlines()

bus_ids = [(index, int(num)) for index, num in enumerate(lines[1].split(',')) if num != 'x']

skip = 1
time = 0

for index, bus_id in bus_ids:
    while True:
        if (time + index) % bus_id == 0:
            break
        time += skip
    skip *= bus_id

print("answer:", time)
