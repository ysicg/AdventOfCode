with open("10.in") as f:
    data = f.read().split("\n")

data.pop()
for i in range(len(data)):
    data[i] = int(data[i])

data.sort()

def chain_adapt():
    outlet = 0
    d1 = 0
    d3 = 0
    for plug in data:
        d =  plug - outlet
        if d == 1:
            d1 += 1
            outlet += d
        elif d == 3:
            d3 += 1
            outlet += d

    
    return d1*(d3+1)

print("Part 1: ", chain_adapt())

# Part 2

"""
Tree Search

Part 1 got us the longest arrangement, consists of only 1 and 3-jolt jumps. Only 1-jolt{>1} jumps allow for different arrangements. 
Total arrangement number *=  combinations of sub-arrays of 1-jolt jumps

"""


def count_diffs( data):

    arr = []
    charger = 0
    for i in range(len(data)):
        d = data[i] - charger
        arr.append(d)
        charger = data[i]

    return arr


def strip(diff_arr):
    # 3-jolt jumps are indivisable -> strip them from array of jumps.
    t = 0
    arr = []
    for e in diff_arr:
        if e == 1:
            t += 1
        elif e == 3:
            if t: 
                arr.append(t)
                t = 0
    if t: 
        arr.append(t)
    return arr




def p2():

    diff_arr = count_diffs(data)
    s = strip(diff_arr)
    p2 = 1
    for x in s:
        if x == 4:
            p2 *= 7
        elif x == 3:
            p2 *= 4
        elif x == 2:
            p2 *= 2
    return p2

print("Part 2: ", p2())
