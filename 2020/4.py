import re

with open("4.in") as f:
    data = f.read().split("\n\n")


pps=[] # passports
vpps=[] # valid pps

for pp in data:
    pp = pp.replace("\n", " ")
    pps.append(pp)



for pp in pps:
    valid = True
    for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if key not in pp:
            valid = False
    if valid: 
        vpps.append(pp)

print("Part 1 =", len(vpps))

# Part 2 

p2 = 0
obj = {}

for pp in vpps:
    index = vpps.index(pp)
    obj[index]={}
    field=pp.split()
    for x in field:
        key, value = x.split(":")
        obj[index][key]=value 

for key in obj:
    pp = obj[key]
    if len(pp["byr"]) != 4 or not (1920 <= int(pp["byr"]) <= 2002):
        continue
    if len(pp["iyr"]) != 4 or not (2010 <= int(pp["iyr"]) <= 2020):
        continue
    if len(pp["eyr"]) != 4 or not (2020 <= int(pp["eyr"]) <= 2030):
        continue

    if pp["hgt"][-2:] != "cm" and pp["hgt"][-2:] != "in":
        continue

    if pp["hgt"][-2:] == "cm":
        if not (150 <= int(pp["hgt"][:-2]) <= 193):
            continue

    if pp["hgt"][-2:] == "in":
        if not (59 <= int(pp["hgt"][:-2]) <= 76):
            continue

    if not re.match(r'^#([0-9]|[a-f]){6}$', pp["hcl"]):
        continue

    if pp["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    if not re.match(r'^[0-9]{9}$', pp["pid"]):
        continue

    p2+=1



print("Part 2 =", p2)
