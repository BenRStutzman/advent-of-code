f = open('Input/3.txt')
grid = f.read().splitlines()
width = len(grid[0])
height = len(grid)

slope_x = 3
slope_y = 1

pos = [0, 0]

treesHit = 0
print(height)

while pos[1] < height:
    spot = grid[pos[1]][pos[0] % width]
    print(spot)
    if spot == '#':
        treesHit += 1
    pos[0] += slope_x
    pos[1] += slope_y

print("answer:", treesHit)
