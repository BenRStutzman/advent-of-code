f = open('Input/14.txt')

lines = f.read().splitlines()
memory = {}

for line in lines:
    if line.startswith('mask'):
        mask = line.split(' ')[2][::-1]
        continue

    part1, null, part2 = line.split(' ')
    mem_location = int(part1[4:part1.find(']')])
    number = int(part2)
    bin_number = bin(mem_location)[:1:-1]
    bin_number += '0' * (36 - len(bin_number))
    bin_numbers = {bin_number}

    for index, digit in enumerate(mask):
        new_bin_numbers = set()
        if digit == 'X':
            for bin_number in bin_numbers:
                opposite_digit = '0' if bin_number[index] == '1' else '1'
                new_bin_number = bin_number[:index] + opposite_digit + bin_number[index + 1:]
                new_bin_numbers.add(new_bin_number)
            bin_numbers = bin_numbers.union(new_bin_numbers)
        elif digit == '1':
            for bin_number in bin_numbers:
                new_bin_number = bin_number[:index] + '1' + bin_number[index + 1:]
                new_bin_numbers.add(new_bin_number)
            bin_numbers = new_bin_numbers
    for bin_number in bin_numbers:
        mem_location = int(''.join(bin_number)[::-1], 2)
        memory[mem_location] = number

print("answer:", sum(memory.values()))
