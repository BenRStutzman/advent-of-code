import itertools as it

f = open('Input/1A.txt')
nums = [int(num) for num in f.read().splitlines()]

for (i, j) in it.combinations(nums, 2):
    if i + j == 2020:
        print("i, j:", i, j)
        print("answer:", i * j)
