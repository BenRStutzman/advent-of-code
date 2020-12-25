import copy

f = open('Input/24.txt')

direction_sets = f.read().splitlines()
grid_size = (len(direction_sets[0]) + 100) * 2

grid = [[0 for i in range(grid_size)] for j in range(grid_size)]
reference_tile = (grid_size // 2, grid_size // 2)

def print_grid(grid):
    for row in grid:
        print(row)

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

def count_adjacent(x, y):
    total = 0
    for (i, j) in ((-1, 0), (1, 0), (1, 1), (0, 1), (0, -1), (-1, -1)):
        row = x + 1
        col = y + j
        if (0 < row < grid_size and 0 < col < grid_size):
            total += grid[x + i][y + j]
    return total

for day in range(100):
    print(day)
    new_grid = copy.deepcopy(grid)
    for i, row in enumerate(grid):
        for j, hex in enumerate(row):
            num_adjacent = count_adjacent(i ,j)
            if hex and (num_adjacent == 0 or num_adjacent > 2):
                new_grid[i][j] = 0
            elif not hex and num_adjacent == 2:
                new_grid[i][j] = 1
    grid = new_grid

print("answer:", sum([sum(row) for row in grid]))
