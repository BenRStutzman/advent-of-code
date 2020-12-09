import re

f = open("Input/4.txt")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def dateIsValid(value, minYear, maxYear):
    if not re.fullmatch("[0-9]{4}", value):
        return False
    if not (minYear <= int(value) <= maxYear):
        return False
    return True

passports = [section.split() for section in f.read().split("\n\n")]
passports = [[field.split(":") for field in passport] for passport in passports]
passports = [{field[0]: field[1] for field in passport} for passport in passports]

valid_passports = 0

for passport in passports:
    print("\n\n", passport)
    for field in required_fields:
        print(field, end=": ")
        if field not in passport:
            break
        else:
            value = passport[field]
            if field == "byr":
                if not dateIsValid(value, 1920, 2002):
                    break
            elif field == "iyr":
                if not dateIsValid(value, 2010, 2020):
                    break
            elif field == "eyr":
                if not dateIsValid(value, 2020, 2030):
                    break
            elif field == "hgt":
                if not re.fullmatch("[0-9]+(cm|in)", value):
                    break
                num = int(value[:-2])
                unit = value[-2:]
                if unit == "cm":
                    if not (150 <= num <= 193):
                        break
                else:
                    if not (59 <= num <= 76):
                        break
            elif field == "hcl":
                if not re.fullmatch("#[0-9a-f]{6}", value):
                    break
            elif field == "ecl":
                if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    break
            elif field == "pid":
                if not re.fullmatch("[0-9]{9}", value):
                    break
        print("valid")
    else:
        valid_passports += 1

print("\n\nanswer:", valid_passports)
