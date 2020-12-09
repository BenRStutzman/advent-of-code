f = open('Input/2.txt')
lines = [line.split() for line in f.read().splitlines()]
validPasswords = 0

for line in lines:
    minTimes, maxTimes = [int(num) for num in line[0].split('-')]
    letter = line[1][0]
    password = line[2]
    print(minTimes, maxTimes, letter, password, end = " ")
    if minTimes <= password.count(letter) <= maxTimes:
        print("valid")
        validPasswords += 1
    else:
        print("invalid")

print("answer:", validPasswords)
