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

def find_a_seat(start_row, start_col, row_dir, col_dir):
    row, col = start_row + row_dir, start_col + col_dir
    while 0 <= row < rows and 0 <= col < cols:
        state = grid[row][col]
        if state == 'L':
            return 0
        elif state == '#':
            return 1
        else:
            row += row_dir
            col += col_dir
    return 0

def calc_next_state(row, col):
    global state_changed
    cur_state = grid[row][col]
    if cur_state == '.':
        return cur_state
    occupied = 0
    for row_dir in range(-1, 2):
        for col_dir in range(-1, 2):
            occupied += find_a_seat(row, col, row_dir, col_dir)
    if cur_state == 'L' and occupied == 0:
        state_changed = True
        return '#'
    elif cur_state == '#' and occupied >= 6:
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
