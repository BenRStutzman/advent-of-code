f = open('Input/23.txt')

cups = [int(num) - 1 for num in list(f.read())[:-1]]
num_cups = len(cups)

print([cup + 1 for cup in cups])

def shuffle(cups, current_index):
    current_cup = cups[current_index]
    print("current:", current_cup + 1)
    shuffled_cups = []
    removal_index = (current_index + 1) % num_cups
    for i in range(3):
        shuffled_cups.append(cups[removal_index])
        removal_index = (removal_index + 1) % num_cups
    print("shuffled:", [cup + 1 for cup in shuffled_cups])
    for cup in shuffled_cups:
        cups.remove(cup)
    destination_cup = (current_cup - 1) % num_cups
    while destination_cup in shuffled_cups:
        destination_cup = (destination_cup - 1) % num_cups
    print("destination:", destination_cup + 1)
    insertion_index = cups.index(destination_cup) + 1
    cups = cups[:insertion_index] + shuffled_cups + cups[insertion_index:]
    print(current_index)
    current_index = (cups.index(current_cup) + 1) % num_cups
    return cups, current_index

current_index = 0

for i in range(100):
    cups, current_index = shuffle(cups, current_index)
    print([cup + 1 for cup in cups], end = '\n\n')

cups = [str(cup + 1) for cup in cups]
index_of_one = cups.index('1')

print("answer:", ''.join(cups[index_of_one + 1:] + cups[:index_of_one]))
