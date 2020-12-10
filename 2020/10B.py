f = open('Input/10.txt')

joltages = sorted([int(num) for num in f.read().splitlines()])
joltages = [0] + joltages

ways_to_get_tos = [1]

for joltage in joltages[1:]:
    ways_to_get_to = 0
    for difference in range(1, 4):
        lower_joltage = joltage - difference
        if lower_joltage in joltages:
            ways_to_get_to += ways_to_get_tos[joltages.index(lower_joltage)]
    ways_to_get_tos.append(ways_to_get_to)

print(ways_to_get_tos)
print("answer:", ways_to_get_tos[-1])
