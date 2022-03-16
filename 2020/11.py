import re
import copy

with open("11.in") as f:
    layout = list(map(list, map(str.rstrip, f.readlines())))




def clamp_r(n):

    lo, hi = 0, len(layout)

    return min(hi, max(lo, n))

def clamp_c(n):

    lo, hi = 0, len(layout[0])

    return min(hi, max(lo, n))


def neighbors(r,c): #row,colomn

    dr = list(range(clamp_r(r-1), clamp_r(r+2)))
    dc = list(range(clamp_c(c-1), clamp_c(c+2)))

    return dr, dc



def round(layout):

    new_layout = copy.deepcopy(layout)
    ROWL = len(layout)
    COLL = len(layout[0])
    for r in range(ROWL):
        for c in range(COLL):
            seat = layout[r][c]
            dr, dc = neighbors(r,c)
            adj_seats = 0
            for i in dr:
                for j in dc:
                    if i == r and j == c:
                        pass
                    elif layout[i][j] == "#":
                        adj_seats+=1
            if seat == "L" and adj_seats == 0:
                new_layout[r][c] = "#"
            elif seat == "#" and adj_seats >= 4:
                new_layout[r][c] = "L"


    return new_layout

def p1(layout):
    layouts = []
    while layout not in layouts:
        layouts.append(layout)
        layout = round(layout)
    return layout

final = (p1(layout))
count = 0
for r in final:
    for seat in r:
        if seat == "#":
            count += 1
print(count)
