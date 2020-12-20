import math
f = open('Input/20.txt')

def print_grid(grid):
    print()
    for row in grid:
        print(row)

def rotate(grid):
    return [[row[i] for row in grid] for i in range(len(grid) - 1, -1, -1)]

def flip(grid):
    return [row[::-1] for row in grid]

def rotate_all(grid):
    for row in grid:
        for tile_index in row:
            if tile_index != '.':
                tiles[tile_index] = rotate(tiles[tile_index])
    return rotate(grid)

def flip_all(grid):
    for row in grid:
        for tile_index in row:
            if tile_index != '.':
                tiles[tile_index] = flip(tiles[tile_index])
    return flip(grid)

raw_tiles = [section.split(':') for section in f.read().split('\n\n')]
tiles = {}

for raw_index, raw_tile in raw_tiles:
    index = int(raw_index.split(' ')[1])
    tile = raw_tile.splitlines()[1:]
    tiles[index] = tile

available_tiles = list(tiles.keys())

edge_size = int(math.sqrt(len(tiles)))
grid = [['.' for i in range(edge_size * 2 - 1)] for i in range(edge_size * 2 - 1)]

grid[edge_size - 1][edge_size - 1] = available_tiles[0]
del available_tiles[0]

def find_a_match(tile):
    global available_tiles
    for available_tile_index in available_tiles:
        available_tile = tiles[available_tile_index]
        for flips in range(2):
            for rotations in range(4):
                if tile[0] == available_tile[-1]:
                    # available tile fits on top
                    tiles[available_tile_index] = available_tile
                    available_tiles.remove(available_tile_index)
                    return available_tile_index
                available_tile = rotate(available_tile)
            available_tile = flip(available_tile)
    return False

def add_tile():
    global grid
    for flips in range(2):
        for rotations in range(4):
            for i, row in enumerate(grid):
                for j, tile_index in enumerate(row):
                    if tile_index != '.':
                        matching_tile_id = find_a_match(tiles[tile_index])
                        if matching_tile_id:
                            grid[i - 1][j] = matching_tile_id
                            print_grid(grid)
                            return
            grid = rotate_all(grid)
        grid = flip_all(grid)

while(available_tiles):
    add_tile()

for i in range(len(grid)):
    grid[i] = [index for index in grid[i] if index != '.']

grid = [row for row in grid if row]

print_grid(grid)

print("answer:", grid[0][0] * grid[0][-1] * grid[-1][0] * grid[-1][-1])
