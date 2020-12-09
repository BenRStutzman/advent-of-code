f = open('Input/5.txt')

lines = f.read()
lines = lines.replace('F', '0').replace('B', '1')
lines = lines.replace('L', '0').replace('R', '1')
binaries = lines.splitlines()

maxId = 994

seatIds = [int(binary, 2) for binary in binaries]

for id in range(maxId, 0, -1):
    if id not in seatIds:
        print("answer:", id)
        break
