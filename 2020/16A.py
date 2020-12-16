f = open('Input/16.txt')

sections = f.read().split('\n\n')
valid_range_pairs = []

for line in sections[0].splitlines():
    parts = line.split(' ')
    range1 = [int(num) for num in parts[-3].split('-')]
    range2 = [int(num) for num in parts[-1].split('-')]
    valid_range_pairs.append((range1, range2))

my_ticket = [int(num) for num in sections[1].splitlines()[1].split(',')]

nearby_tickets = [[int(num) for num in line.split(',')] for line in sections[2].splitlines()[1:]]

sum_invalid = 0

for ticket in nearby_tickets:
    for field in ticket:
        for valid_range_pair in valid_range_pairs:
            for valid_range in valid_range_pair:
                if valid_range[0] <= field <= valid_range[1]:
                    break
            else:
                continue
            break
        else:
            sum_invalid += field

print("answer:", sum_invalid)
