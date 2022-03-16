import re 

with open("19.t") as f:
    rules, msgs = f.read().strip().split("\n\n")

rules, msgs = rules.split("\n"), msgs.split("\n")

R = {}
for rule in rules:
    k, v  = rule.split(":")
    R[k] = v.strip().strip('"')


pattern = re.compile(r'(\d+)')

ANS = []

'''

R[rule_index] = rule
=> rule refers to other rule_indexes
    R[for rule_index in rule]
    R["0"] = sum_ri R[for rule_index in R["0"]]

'''
def check(ri):
   
    ans = ''
    if not R[ri]:
        return "empty rule"

    if R[ri] == "a" or R[ri] == "b":
        return R[ri]

    elif "|" not in R[ri]:
       new_rules = pattern.findall(R[ri])
       return "".join(list(map(check, new_rules)))
      # for new_rule in new_rules:
      #    ans +=  check(new_rule) 
    
#    elif "|" in R[ri]:
#        r1, r2 = R[ri].split("|")
#        print("r1,r2 = ", r1,r2)
#        return "".join(list(map(check, pattern.findall(r1)))) + "|" + " ".join(list(map(check, pattern.findall(r2))))
#
#       new_rules = pattern.findall(R[rule])
#       for new_rule in new_rules:
#          ans +=  check(new_rule) 
        
    else:
        raise Exception("R[RULE] not expected")

    return ans

        


print( check("0") )
        
#for r,v in R.items(): print(r, " : ",v)

