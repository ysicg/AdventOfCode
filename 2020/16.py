import re

with open("16.in") as f:
    data = f.read().strip()


def p1_format():

    pattern = re.compile(r'(\d+)-(\d+) or (\d+)-(\d+)')
    rules, myticket, tickets = data.split("\n\n")
    rules = rules.strip().split("\n")

    for i in range(len(rules)):
        rules[i] = pattern.findall(rules[i])[0]
        rules[i] = list(map(int, rules[i]))

    _, myticket = myticket.split(":")
    _, tickets = tickets.split(":")
    tickets = tickets.strip().split("\n")

    for i in range(len(tickets)):
        tickets[i] = tickets[i].split(",")
        tickets[i] = list(map(int, tickets[i]))

    return tickets, rules


def sum_of_invalid_tickets():
    invalid = []
    tickets, rules = p1_format()
    for ticket in tickets:
        for value in ticket:
            valid = False
            for rule in rules:
                if rule[0] <= value <= rule[1] or rule[2] <= value <= rule[3]:
                    valid = True
                    break
            if not valid:
                invalid.append(value)
    return sum(invalid)
                
#print("Part 1 = ", sum_of_invalid_tickets())


# Part 2


def keep_valid_tickets():
    valid_tickets = []
    tickets, rules = p1_format()
    for ticket in tickets:
        valid_ticket = True
        for value in ticket:
            valid_value = False
            for rule in rules:
                if rule[0] <= value <= rule[1] or rule[2] <= value <= rule[3]:
                    valid_value = True
                    break
            if not valid_value:
                valid_ticket = False
                break

        if valid_ticket:
            valid_tickets.append(ticket)
    print("valid_tickets", len(valid_tickets))

    return valid_tickets, rules



def p2():
    tickets, rules = keep_valid_tickets()
    #tickets = tickets[:10]
    rules = rules[7:12]
    indexes = {}
    ticket_size = len(tickets[0])
    for r in range(len(rules)):
        print(r)
        rule = rules[r]
        t_ind = int('1'*ticket_size, 2)
        for ticket in tickets:
            index = 0
            for v in ticket:
                if rule[0] <= v <= rule[1] or rule[2] <= v <= rule[3]:
                    index += 2**(ticket_size -1 - ticket.index(v))
            print("TICKET NUMBER: ", tickets.index(ticket))
            print("rule", rule)
            print("ticket", ticket)
            print("index", index)
            t_ind = t_ind & index
            print("t_ind", t_ind)
            if t_ind == 0:
                print("RULES INDEX = ", r)
                raise Exception("0")
                    
        indexes[r] = bin(t_ind)[2:].zfill(ticket_size)

    print("number of tickets", len(tickets))
    print("number of rules", len(rules))

    return indexes
inds = p2()

print(inds)
