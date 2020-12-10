f = open('Input/10.txt')

joltages = sorted([int(num) for num in f.read().splitlines()])

last_joltage = 0
differences = {1: 0, 2: 0, 3: 1}

for joltage in joltages:
    differences[joltage - last_joltage] += 1
    last_joltage = joltage

print(differences)
print("answer:", differences[1] * differences[3])
