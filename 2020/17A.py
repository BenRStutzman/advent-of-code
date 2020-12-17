import copy

f = open('Input/17.txt')

def print_matrix(matrix):
    for index, plane in enumerate(matrix):
        print('\nx=' + str(index))
        for line in plane:
            print(''.join(line))

def expand(matrix):
    new_dim = len(matrix[0]) + 2
    empty_line = ['.' for i in range(new_dim)]
    empty_plane = [empty_line[:] for i in range(new_dim)]
    new_matrix = [copy.deepcopy(empty_plane)]
    for plane in matrix:
        new_plane = [empty_line[:]]
        for line in plane:
            new_plane.append(['.'] + line + ['.'])
        new_plane.append(empty_line[:])
        new_matrix.append(new_plane)
    new_matrix.append(copy.deepcopy(empty_plane))
    return new_matrix

def count_neighbors(x, y, z):
    global matrix
    total_neighbors = 0
    for i in range(max(0, x - 1), min(len(matrix), x + 2)):
        for j in range(max(0, y - 1), min(len(matrix[0]), y + 2)):
            for k in range(max(0, z - 1), min(len(matrix[0][0]), z + 2)):
                total_neighbors += matrix[i][j][k] == '#'
    total_neighbors -= matrix[x][y][z] == '#'
    return total_neighbors

def next_state(x, y, z):
    global num_activated
    global matrix
    cur_state = matrix[x][y][z]
    neighbors = count_neighbors(x, y, z)
    if cur_state == '#':
        next_state = '#' if 2 <= neighbors <= 3 else '.'
    else:
        next_state = '#' if neighbors == 3 else '.'
    num_activated += next_state == '#'
    return next_state

matrix = [[list(line) for line in f.read().splitlines()]]
print('------- Starting matrix: -------')
print_matrix(matrix)

for cycle in range(6):
    num_activated = 0
    matrix = expand(matrix)
    new_matrix = copy.deepcopy(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for z in range(len(matrix[0][0])):
                new_matrix[x][y][z] = next_state(x, y, z)
    matrix = new_matrix
    print('\n------- After cycle ' + str(cycle + 1) + ': -------')
    print_matrix(matrix)
    print('(' + str(num_activated) + ' activated)')
