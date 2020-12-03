with open("3.in") as f:
    data = f.read().split("\n")
data.pop()


def counter(r,d):
    tree_count = 0
    s=0
    width = len(data[0])
    for i in range(0, len(data), d):
        if data[i][s % width] == "#": 
            tree_count += 1 
        s += r
    return tree_count

result = counter(1,1)*counter(3,1)*counter(5,1)*counter(7,1)*counter(1,2)
print(result)
