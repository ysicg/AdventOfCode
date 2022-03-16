with open("8.in") as f:
    data = f.read().strip().split("\n")


def boot():
    i = 0
    acc = 0
    l = []
    while i < len(data):
        x, y = data[i].split(" ")
        if i in l[:-1]:
            return acc
        if x == "acc":
            acc += int(y)
            i += 1
        elif x == "jmp":
            i += int(y)
        else:
            i += 1

        l.append(i)

print("part 1: ", boot())

def repair(data, changed):
    i = 0
    acc = 0
    l = []
    print(changed)
    while i < len(data):
        x, y = changed[i].split(" ")
        if i in l[:-1]:
            print("1")
            for j in range(len(data)):
                if "jmp" in changed[-j]:
                    print("HERE")
                    changed[-j] = data[-j].replace("jmp", "nop")
                    print("changed", changed)
                    return repair(data,changed )

        elif x == "acc":
            print("acc")
            acc += int(y)
            i += 1
        elif x == "jmp":
            print("nop")
            i += int(y)
        else:
            i += 1

        l.append(i)
    return acc

#print("part 2: ", repair(data, data))
