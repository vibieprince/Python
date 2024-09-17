# get
# keys
# values
# items
# del
# pop
# dict
# update
# clear
#
d = {'course': 'python',
     'fees': 8000,
     'duration': '2 months'
     }
print()
n = d.get("course")
print(n)

for a in d.keys():
    print(a)

for a in d.values():
    print(a)

for i in d.items():
    print(i)

del d["course"]
print(d)

d.pop("duration")
print(d)

d=dict(name='python',fees=8000)
print(d)

d.update({'fees':100000})
print(d)

#d.clear()
#print(d)

d['disc']="This is python"
print(d)





