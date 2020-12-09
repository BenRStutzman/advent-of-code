f = open('Input/3.txt')
grid = f.read().splitlines()
width = len(grid[0])
height = len(grid)

def treesHit(stepsRight, stepsDown):
    slope_x = stepsRight
    slope_y = stepsDown

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

    return treesHit

treesHitArray = []

for stepsRight, stepsDown in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    treesHitArray.append(treesHit(stepsRight, stepsDown))

print(treesHitArray)
product = 1
for treesHit in treesHitArray:
    product *= treesHit

print(product)
