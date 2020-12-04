f = open("Input/4.txt")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passports = [section.split() for section in f.read().split("\n\n")]
passports = [[field.split(":")[0] for field in fields] for fields in passports]

valid_passports = 0

for passport in passports:
    for required_field in required_fields:
        if required_field not in passport:
            break
    else:
        valid_passports += 1

print("answer:", valid_passports)
