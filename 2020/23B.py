from collections import deque

f = open('Input/23.txt')

num_cups = 1000000
num_shuffles = 10000000

cups_to_insert = { i : [] for i in range(num_cups) }

cups = deque([int(num) - 1 for num in list(f.read())[:-1]])
for i in range(len(cups), num_cups):
    cups.append(i)

def next_cup():
    global cup
    to_be_inserted = cups_to_insert[cup]
    while to_be_inserted:
        cups.appendleft(to_be_inserted.pop())
    cup = cups.popleft()
    return cup

cup = cups.popleft()

for i in range(num_shuffles):
    destination_cup = (cup - 1) % num_cups
    cups.append(cup)
    to_be_inserted = [next_cup(), next_cup(), next_cup()]
    while destination_cup in to_be_inserted:
        destination_cup = (destination_cup - 1) % num_cups
    cups_to_insert[destination_cup] = to_be_inserted
    next_cup()

while cup != 0:
    next_cup()

print("answer:", (next_cup() + 1) * (next_cup() + 1))
