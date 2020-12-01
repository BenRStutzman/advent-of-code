import itertools as it

f = open('Input/1A.txt')
nums = [int(num) for num in f.read().splitlines()]

for (i, j, k) in it.combinations(nums, 3):
    if i + j + k == 2020:
        print("i, j, k:", i, j, k)
        print("answer:", i * j * k)
