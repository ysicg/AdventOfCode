import re 

with open("20.in") as f:
    data = f.read().strip().split("\n\n")

for i in range(len(data)):
    data[i] = data[i].split("\n")
    

tiles = dict()

p = re.compile('\d+')

for d in data:
    key = int(p.findall(d[0])[0])
    value = d[1:]
    tiles[key] = value


print(tiles)

