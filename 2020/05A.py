f = open('Input/5.txt')

lines = f.read()
lines = lines.replace('F', '0').replace('B', '1')
lines = lines.replace('L', '0').replace('R', '1')
binaries = lines.splitlines()

maxId = 0

for binary in binaries:
    seatId = int(binary, 2)
    maxId = max(seatId, maxId)

print("answer:", maxId)
