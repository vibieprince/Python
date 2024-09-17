t=(3,2,5,6,7,8,4,3,6,8,8,4,2)
print(type(t))
n=t[3]
print(n)
print()
m=min(t)
print(m)
n=max(t)
print(n)
p=t.count(3)
print(p)
o=t.index(4)
print(o)
print()
s=sum(t)
print(s)
j=sum(t,10)
print(j)
print()
l=len(t)
print(l)
for x in range(l):
    print(t[x])
print()

    #OR
for a in t:
    print(a)