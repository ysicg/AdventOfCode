import re


with open("7.in") as f:
    data = f.read().splitlines()


children = set()
outer_bags = set()


def p1(bags, counter):
    parent = []
    for bag in bags:
        if bag not in children:
            for line in data:
                if re.findall(r'(?<!^)'+bag, line):
                   parent.append(re.findall(r'^\w+ \w+', line)[0])
                elif counter : 
                    outer_bags.add(bag)
            children.add(bag)
    if parent:
        p1(parent, 1)


print(p1(["shiny gold"], 0))

#print(len(outer_bags))


# Part 2


def p2(bag):
    count = 0
    fact = int(bag[0])
    print("bag : ", bag)
    print("fact = ", fact)
    for line in data:  
        if re.findall(r'^'+bag[2:], line):
            pattern = re.findall(r'\d+ \w+ \w+', line)
            print("pattern = ", pattern)
            if not pattern: 
                print("empty bag : ", bag)
                print("empty count", fact)
                return fact
            if pattern:
                for p in pattern:
                    count += fact*(p2(p)+1)
                    print("bag : ", bag)
                    print("p : ", p)
                    print("count", fact*(p2(p)+1))
            break
    return count



#print("part 2: ", p2("1 shiny gold"))
