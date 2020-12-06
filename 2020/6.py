with open("6.in") as f:
    data = f.read().split('\n\n')

data[-1]=data[-1][:-1] #get rid of trailing "\n"

# Part 1

p1=0

for entry in data:
    p1 += len(set(x for x in entry.replace("\n","")))

print(p1)


# Part 2

p2=0

for group in data:
    persons = group.split("\n")
    for ans in persons[0]:
        if group.replace("\n", "").count(ans) == len(persons):
            p2+=1

print(p2)



