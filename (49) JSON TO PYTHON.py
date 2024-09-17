import json
d='{"course":"python","fees": 12000,"duration":"2 months"}'
x=json.loads(d)
print(x,type(x))
for a in x:
    print(a,x[a])

