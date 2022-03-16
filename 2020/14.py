import time
import re
import pdb

startTime = time.time()

with open("14.t2") as f:
    data = f.read().strip().split("\n")

get_bin = lambda x, n: format(x, 'b').zfill(n)

def value2binary():
    program = []
    for d in data:
        key, value = d.split(" = ")
        program.append((key, value) if key == "mask" else (key, get_bin(int(value), 36)))
    return program

def all2binary():
    program = []
    for d in data:
        key, value = d.split(" = ")
        program.append((key, value) if key == "mask" else (get_bin(int(re.search(r'\d+', key).group() ), 36), get_bin(int(value), 36)))
    return program

memory = {}

def p1():
    program = value2binary()
    ans = 0
    for t in program:
        if t[0] == "mask":
            mask = t[1]
        else: 
            key = re.search(r'\d+', t[0]).group()
            value = ''
            for i in range(36):
                if mask[i] == "X":
                    value += t[1][i]
                else:
                    value += mask[i]
            memory[key] = int(value, 2)
    for x in memory.values():
        ans +=x
    return ans

#print(p1())

# Part 2


def X(key, keys):

    if time.time() - startTime  > 10:
        print(time.time())
        raise Exception("too long")

    if key.count("X") == 0:
        keys.append(key)
        return keys
    print("KEY to replace by 0 : ", key)
    keys += X(key.replace("X", "0", 1), keys)
    print("KEY to replace by 1 : ", key)
    keys += X(key.replace("X", "1", 1), keys)

    
    return keys

def p2():
    program = all2binary()
    ans = 0
    for t in program:
        if t[0] == "mask":
            mask = t[1]
            continue
        else: 
            value = t[1]
            keys = []
            key = list(t[0])

            for k in range(len(key)):
                if time.time() - startTime  > 10:
                    print(time.time())
                    raise Exception("too long")
                if mask[k] == "1":
                    key[k] = "1"
                elif mask[k] == "X":
                    key[k] = "X"

            key = "".join(key)
            
            print("KEY before calling X : ", key)
            keys = X(key, keys)
            
            for k in keys:
                #print("".join(k[-6:]))
                memory[k] = int(value, 2)
    print("KEYS" )
    for k in keys[:5]:
        print(k)

    print("SIZE OF MEMORY :", len(memory))
    for x in memory.values():
        print(x)
        ans +=x
    return ans

#pdb.set_trace()
print(p2())

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
