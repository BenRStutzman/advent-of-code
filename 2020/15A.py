f = open('Input/15.txt')

numbers = [int(num) for num in f.read().split(",")][::-1]

while len(numbers) < 2020:
    try:
        next_num = numbers[1:].index(numbers[0]) + 1
    except ValueError:
        next_num = 0
    numbers = [next_num] + numbers[:]

print("answer:", next_num)
