import re

with open("18.in") as f:
    data = f.read().strip().split("\n")

data = [data[0]]

paren = re.compile(r'(?<=\()([0-9\+\*\ ]*)(?=\))')

def eval_paren():

    for line in data:
        print(tuple(map(eval,paren.findall(line))))

eval_paren()


