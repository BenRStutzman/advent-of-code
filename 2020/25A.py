f = open('Input/25.txt')

public_keys = [int(num) for num in f.read().splitlines()]
print(public_keys)

loop_size = 1
value = 1
while True:
    value *= 7
    value %= 20201227
    if value == public_keys[0]:
        break
    loop_size += 1

print(loop_size)

value = 1
for i in range(loop_size):
    value *= public_keys[1]
    value %= 20201227

print("answer:", value)
