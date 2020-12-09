f = open('Input/6.txt')

groups = f.read().split('\n\n');

total = 0

for group in groups:
    lines = group.strip().split('\n')
    yeses = set(lines[0])
    for line in lines[1:]:
        yeses = yeses.intersection(set(line))

    num_yeses = len(yeses)
    print(num_yeses)
    total += num_yeses

print("answer:", total)
