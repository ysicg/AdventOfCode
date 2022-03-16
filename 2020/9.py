with open("9.in") as f:
    data = f.read().split("\n")

data.pop()

for i in range(len(data)): 
        data[i]=int(data[i])

def p1(p=25):
    for i in range(p, len(data)):
        sumExists = False
    
        for j in range(i-p, i):
    
            for k in range(i-p,i):
                if not k==j and data[k]+data[j]==data[i]:
                    sumExists = True
                    break
    
            if sumExists:
                break
    
        if not sumExists:
            return data[i]
            break
    return 0

print("Part 1: ", p1())


## Part 2

def p2(p1):

    for i in range(len(data)):
        s=data[i]
        j=i

        while s<=p1:

            if  s==p1:
                return min(data[i:j+1])+max(data[i:j+1])

            s+=data[j+1]
            j+=1

    return 0


print("Part 2: ", p2(p1()))
