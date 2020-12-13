f = open('Input/13.txt')

lines = f.read().splitlines()

earliest_time = int(lines[0])
bus_ids = [int(num) for num in lines[1].split(',') if num != 'x']

shortest_wait = min(bus_ids)
bus_to_catch = min(bus_ids)

for bus_id in bus_ids:
    wait = bus_id - (earliest_time % bus_id)
    if wait < shortest_wait:
        shortest_wait = wait
        bus_to_catch = bus_id

print(bus_to_catch, shortest_wait)
print("answer:", bus_to_catch * shortest_wait)
