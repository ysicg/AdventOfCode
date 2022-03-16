with open("13.in") as f:
    data = f.read().split("\n")

#buses = []
#for bus in data[1].split(","):
#    if bus != "x":
#        buses.append(int(bus))
#
#station = int(data[0])
#
#table = {}
#for bus in buses:
#    table[bus] = station - station % bus + bus
#
#bus_id = min(table, key=table.get)
#print("p1", bus_id*(table[bus_id] - station))

#part 2

d = data[1].split(",")
bus = {}
for i in range(len(d)):
    if d[i] != "x":
        bus[int(i)] = int(d[i])

keys = sorted(bus.keys())

print(bus)

def p2():
    print("bus :", bus)
    tf = 1
    for key, value in bus.items():
        if value == max(bus.values()):
            tf *=key+value
    print("tf = ", tf)
    t = 0
    p2 = 0
    while True:
        #if (t + keys[j]) % bus[keys[j]] == 0:
        #    print("(t + keys[j]) % bus[keys[j]] : (", t,  "+", keys[j], ") %", bus[keys[j]])
        #    #tf = keys[j]
        #    j += 1
        #    print(j)
        #if j == len(keys):
        #    break
        count=0
        for i in keys:
            if (t + i) % bus[i] == 0:
                count+=1
                print(count)
        if count == len(keys):
            return t

        t += tf 

        
#print("part 2 : ", p2())
product = 1
for key, value in bus.items():
    product *= value
print(product)





#t = 0
#t += factor # factor multiple of keys[0]
#
#if (t + keys[1]) % bus[keys[1]]:
#    (t + keys[1] - keys[1]) % bus[keys[0]]
#t = factor











