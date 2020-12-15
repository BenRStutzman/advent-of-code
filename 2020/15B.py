f = open('Input/15.txt')

numbers = [int(num) for num in f.read().split(",")]
spoken_numbers = {num: index + 1 for index, num in enumerate(numbers[:-1])}
last_num = numbers[-1]

index = len(numbers)

while index < 30000000:
    last_index = spoken_numbers.get(last_num)
    spoken_numbers[last_num] = index
    last_num = index - last_index if last_index else 0
    index += 1

print("answer:", last_num)
