import itertools as it

f = open('Input\9.txt')

preamble_length = 25

numbers = [int(num) for num in f.read().splitlines()]

for index, number in enumerate(numbers[preamble_length:]):
    previous_numbers = numbers[index : index + preamble_length]
    all_sums = [(num1 + num2) for num1, num2 in it.combinations(previous_numbers, 2)]
    if number not in all_sums:
        print("answer:", number)
        break
