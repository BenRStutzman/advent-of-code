f = open('Input/2A.txt')
lines = [line.split() for line in f.read().splitlines()]
validPasswords = 0

for line in lines:
    pos1, pos2 = [int(num) for num in line[0].split('-')]
    letter = line[1][0]
    password = line[2]
    print(pos1, pos2, letter, password, end = " ")
    if (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter):
        print("valid")
        validPasswords += 1
    else:
        print("invalid")

print("answer:", validPasswords)
