f = open('Input/14.txt')

lines = f.read().splitlines()
memory = {}

for line in lines:
    if line.startswith('mask'):
        mask = line.split(' ')[2][::-1]
        continue
    part1, blah, part2 = line.split(' ')
    mem_location = int(part1[4:part1.find(']')])
    number = int(part2)
    bin_number = bin(number)[:1:-1]
    bin_number += '0' * (36 - len(bin_number))
    bin_number = list(bin_number)
    for index, digit in enumerate(mask):
        if digit == '1':
            bin_number[index] = '1'
        elif digit == '0':
            bin_number[index] = '0'
    memory[mem_location] = int(''.join(bin_number)[::-1], 2)

print(memory)
print("answer:", sum(memory.values()))
