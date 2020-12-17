import copy

f = open('Input/17.txt')

def print_matrix(matrix):
    for index, grid in enumerate(matrix):
        for jindex, plane in enumerate(grid):
            print('\nw=' + str(index) + ', x=' + str(jindex))
            for line in plane:
                print(''.join(line))

def expand(matrix):
    empty_line = ['.' for i in range(len(matrix[0][0][0]) + 2)]
    empty_plane = [empty_line[:] for i in range(len(matrix[0][0]) + 2)]
    empty_grid = [copy.deepcopy(empty_plane) for i in range(len(matrix[0]) + 2)]
    new_matrix = [copy.deepcopy(empty_grid)]
    for grid in matrix:
        new_grid = [copy.deepcopy(empty_plane)]
        for plane in grid:
            new_plane = [empty_line[:]]
            for line in plane:
                new_plane.append(['.'] + line + ['.'])
            new_plane.append(empty_line[:])
            new_grid.append(new_plane)
        new_grid.append(copy.deepcopy(empty_plane))
        new_matrix.append(new_grid)
    new_matrix.append(copy.deepcopy(empty_grid))
    return new_matrix

def count_neighbors(w, x, y, z):
    global matrix
    total_neighbors = 0
    for h in range(max(0, w - 1), min(len(matrix), w + 2)):
        for i in range(max(0, x - 1), min(len(matrix[0]), x + 2)):
            for j in range(max(0, y - 1), min(len(matrix[0][0]), y + 2)):
                for k in range(max(0, z - 1), min(len(matrix[0][0][0]), z + 2)):
                    total_neighbors += matrix[h][i][j][k] == '#'
    total_neighbors -= matrix[w][x][y][z] == '#'
    return total_neighbors

def next_state(w, x, y, z):
    global num_activated
    global matrix
    cur_state = matrix[w][x][y][z]
    neighbors = count_neighbors(w, x, y, z)
    if cur_state == '#':
        next_state = '#' if 2 <= neighbors <= 3 else '.'
    else:
        next_state = '#' if neighbors == 3 else '.'
    num_activated += next_state == '#'
    return next_state

matrix = [[[list(line) for line in f.read().splitlines()]]]
print('------- Starting matrix: -------')
print_matrix(matrix)

for cycle in range(6):
    num_activated = 0
    matrix = expand(matrix)
    print_matrix(matrix)
    new_matrix = copy.deepcopy(matrix)
    for w in range(len(matrix)):
        for x in range(len(matrix[0])):
            for y in range(len(matrix[0][0])):
                for z in range(len(matrix[0][0][0])):
                    new_matrix[w][x][y][z] = next_state(w, x, y, z)
    matrix = new_matrix
    print('\n------- After cycle ' + str(cycle + 1) + ': -------')
    print_matrix(matrix)
    print('(' + str(num_activated) + ' activated)')
