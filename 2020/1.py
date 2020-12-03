with open("1.in") as f:
    data = f.read().split("\n")
data.pop()

# Part 1

def p1(data):
    for n1 in data:
        for n2 in data:
            if int(n1) + int(n2) == 2020:
                return int(n1) * int(n2)

#print(p1(data))

# Part 2

def p2(data):
    for n1 in data:
        for n2 in data:
            for n3 in data:
                if int(n1) + int(n2) + int(n3) == 2020:
                    return int(n1) * int(n2) * int(n3)

print(p2(data))
