f = open('Input/10.txt')

joltages = [0] + sorted([int(num) for num in f.read().splitlines()])

ways_to_get_tos = [1]

for index, joltage in enumerate(joltages[1:]):
    ways_to_get_to = 0
    for lower_index in range(max(0, index - 2), index + 1):
        if joltage - joltages[lower_index] <= 3:
            ways_to_get_to += ways_to_get_tos[lower_index]
    ways_to_get_tos.append(ways_to_get_to)

print(ways_to_get_tos)
print("answer:", ways_to_get_tos[-1])
