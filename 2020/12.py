import numpy as np
import math

with open("12.in") as f:
    data = f.read().split("\n")
data.pop()

#face = 90

# Convert rotations to translations

#for i in range(len(data)):
#
#    if data[i][0] == "L":
#        face -= int(data[i][1:])
#    elif data[i][0] == "R":
#        face += int(data[i][1:])
#    face = face % 360
#    #print(face)
#    if data[i][0] == "F":
#        if face == 90:
#            data[i] = data[i].replace(data[i][0],"E")
#        elif face == 180:
#            data[i] = data[i].replace(data[i][0],"S")
#        elif face == 270:
#            data[i] = data[i].replace(data[i][0],"W")
#        elif face == 0:
#            data[i] = data[i].replace(data[i][0],"N")
#
#
#
#x = 0
#y = 0
#
#for i in data:
#    if i[0] == "E": x += int(i[1:])
#    elif i[0] == "W": x -= int(i[1:])
#    elif i[0] == "N": y += int(i[1:])
#    elif i[0] == "S": y -= int(i[1:])
#
#print("p1", abs(x) + abs(y))

# part 2:



def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return rho, phi

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y

#test

def p2():
    wp = [10,1]
    pos = [0,0]

    for i in range(len(data)):

        action = data[i][0]
        value = int(data[i][1:])
        if action == "N":
            wp[1] += value
        elif action == "S":
            wp[1] -= value
        elif action == "E":
            wp[0] += value
        elif action == "W":
            wp[0] -= value
        elif action == "R":
            x,y = wp
            rho, phi = cart2pol(x,y)
            x,y = list(pol2cart(rho, phi - math.radians(value)))
            wp = [round(x), round(y)]
        elif action == "L":
            x,y = wp
            rho, phi = cart2pol(x,y)
            x,y = list(pol2cart(rho, phi + math.radians(value)))
            wp = [round(x), round(y)]
        elif action == "F":
                pos[0] += value*wp[0]
                pos[1] += value*wp[1]
                    
    return abs(pos[0]) + abs(pos[1])

print("p2", p2())
