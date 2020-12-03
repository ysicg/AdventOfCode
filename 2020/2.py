with open("2.in") as f:
    data = f.read().split("\n")
data.pop()

# Part 1

result=0
for line in data:
    item = line.split(" ")
    a,b=item[0].split("-")
    c=item[1].strip(":")
    pwd = item[2]
    #if (pwd.count(c) >= int(a) and pwd.count(c) <= int(b)):
        #result += 1

    # Part 2
    if (pwd[int(a)-1] == c) != (pwd[int(b)-1] == c):
        result+=1 

print(result)





