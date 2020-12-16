f = open('Input/16.txt')

sections = f.read().split('\n\n')
valid_range_pairs = {}

for line in sections[0].splitlines():
    parts = line.split(':')
    raw_ranges = parts[1].split(' ')
    range1 = [int(num) for num in raw_ranges[1].split('-')]
    range2 = [int(num) for num in raw_ranges[3].split('-')]
    valid_range_pairs[parts[0]] = (range1, range2)

my_ticket = [int(num) for num in sections[1].splitlines()[1].split(',')]

nearby_tickets = [[int(num) for num in line.split(',')] for line in sections[2].splitlines()[1:]]
valid_tickets = []

def field_is_valid(valid_range_pair, field):
    for valid_range in valid_range_pair:
        if valid_range[0] <= field <= valid_range[1]:
            # the field is valid for this range
            break
    else:
        # the field is invalid for this range pair
        return False
    return True

for ticket in nearby_tickets:
    for field in ticket:
        for valid_range_pair in valid_range_pairs.values():
            if field_is_valid(valid_range_pair, field):
                break
        else:
            # the field is invalid for all range pairs
            break
    else:
        # the field is valid for some range pair
        valid_tickets.append(ticket)

all_possible_positions = {}
num_fields = len(valid_range_pairs)

for field_name, valid_range_pair in valid_range_pairs.items():
    possible_positions = []
    for i in range(num_fields):
        for ticket in valid_tickets:
            if not field_is_valid(valid_range_pair, ticket[i]):
                break
        else:
            possible_positions.append(i)
    all_possible_positions[field_name] = possible_positions

positions = {}

for field_name, possible_positions in sorted(all_possible_positions.items(), key = lambda pair: len(pair[1])):
    for possible_position in possible_positions:
        if possible_position not in positions.values():
            positions[field_name] = possible_position
            break

departure_product = 1

for field_name, position in sorted(positions.items(), key = lambda pair: pair[1]):
    print(position + 1, end = ': ')
    print(field_name)
    if field_name.startswith("departure"):
        departure_product *= my_ticket[position]

print()
print("answer:", departure_product)
