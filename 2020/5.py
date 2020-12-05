with open("5.in") as f:
    data = f.read().split("\n")

data.pop()

IDs = []
seatIDs= []

for seat in data:

    lo,up = 0, 127 #rows
    l, r = 0, 7 #columns

    for c in seat[:-3]:
        if c == "F":
            lo, up = lo, int((up-lo-1)/2) + lo
        elif c == "B":
            lo, up = lo + int((up-lo+1)/2), up

    for c in seat[-3:]:
        if c == "L":
            l, r = l, int((r-l-1)/2) + l
        elif c == "R":
            l, r = l + int((r-l+1)/2), r

    IDs.append(lo*8+l)

print("Part 1: ",max(IDs))

# Part 2

IDs = sorted(IDs)

for i in range(len(IDs)-1):
    if IDs[i+1]-IDs[i] ==2:
        print("Part 2: ",IDs[i]+1)
    
