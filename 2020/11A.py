f = open('Input/11.txt')

grid = [[cell for cell in line] for line in f.read().splitlines()]

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end='')
        print('')
    print('')

print_grid(grid)

rows = len(grid)
cols = len(grid[0])

next_grid = [['.' for col in row] for row in grid]

def calc_next_state(row, col):
    global state_changed
    cur_state = grid[row][col]
    if cur_state == '.':
        return cur_state
    occupied = 0
    for adj_row in range(max(0, row - 1), min(rows, row + 2)):
        for adj_col in range(max(0, col - 1), min(cols, col + 2)):
            occupied += grid[adj_row][adj_col] == '#'
    if cur_state == 'L' and occupied == 0:
        state_changed = True
        return '#'
    elif cur_state == '#' and occupied >= 5:
        state_changed = True
        return 'L'
    else:
        return cur_state

state_changed = True

while state_changed:
    state_changed = False
    for row in range(rows):
        for col in range(cols):
            next_grid[row][col] = calc_next_state(row, col)
    print_grid(next_grid)
    grid = [[col for col in row] for row in next_grid]

print(sum([row.count('#') for row in grid]))
