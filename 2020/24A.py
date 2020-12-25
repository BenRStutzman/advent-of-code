f = open('Input/24.txt')

direction_sets = f.read().splitlines()
grid_size = len(direction_sets[0]) * 2

grid = [[0 for i in range(grid_size)] for j in range(grid_size)]
reference_tile = (grid_size // 2, grid_size // 2)

def print_grid(grid):
    for row in grid:
        print(row)

print(reference_tile)
print_grid(grid)

for direction_set in direction_sets:
    x, y = reference_tile
    direction = ''
    for letter in direction_set:
        direction += letter
        if direction in 'ns':
            continue
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
        elif direction == 'ne':
            y += 1
            x += 1
        elif direction == 'nw':
            y += 1
        elif direction == 'se':
            y -= 1
        elif direction == 'sw':
            y -= 1
            x -= 1
        direction = ''
    grid[x][y] = not grid[x][y]

print_grid(grid)
print("answer:", sum([sum(row) for row in grid]))
