with open("15.in") as f:
    data = f.read().strip().split(",")
print(data)

num = [int(x) for x in data]
original_size = len(num)
l = []
for i in range(30000000):
    if i < len(num):
        l.append(num[i])
    elif l.count(l[-1]) == 1:
        l.append(0)
    elif l.count(l[-1]) > 1:
        nd2last = len(l) -1 - list(reversed(l[:-1])).index(l[-1])
        l.append(i - nd2last)

print(l[-1])

    


