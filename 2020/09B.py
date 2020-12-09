f = open('Input\9.txt')

#goal_sum = 127
goal_sum = 1930745883

numbers = [int(num) for num in f.read().splitlines()]

def find_range(numbers, goal_sum):
    for i in range(len(numbers)):
        j = i + 1
        while True:
            cur_range = numbers[i:j + 1]
            cur_sum = sum(cur_range)
            if cur_sum == goal_sum:
                return cur_range
            elif cur_sum > goal_sum:
                break
            else:
                j += 1

goal_range = find_range(numbers, goal_sum)
print(goal_range)
print("answer:", min(goal_range) + max(goal_range))
