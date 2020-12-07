f = open('Input/7.txt')

rules = {}

for line in f.read().splitlines():
    bag_type = line[:line.find(' bags')]
    print(bag_type)
    contained_types = []
    raw_contained_types = line[line.find('contain ') + len('contain '):]
    if raw_contained_types == "no other bags.":
        rules[bag_type] = []
        continue
    for raw_contained_type in raw_contained_types.split(', '):
        split_line = raw_contained_type.split()
        number = int(split_line[0])
        contained_type = split_line[1] + " " + split_line[2]
        contained_types.append((number, contained_type))
    print(contained_types)
    rules[bag_type] = contained_types

total_bags = 0

last_checked = [(1, "shiny gold")]
next_to_check = []

while last_checked:
    for number, bag_type in last_checked:
        for contained_number, contained_type in rules[bag_type]:
            next_to_check.append((number * contained_number, contained_type))
    print(next_to_check)
    total_bags += sum([pair[0] for pair in next_to_check])
    last_checked = next_to_check
    next_to_check = []

print("answer:", total_bags)
