#SETS HAVE VALUES ONLY
#IT IS DEFINED BY CURLY BRACKETS
#SET HAVE UNIKE ELEMENTS ONLY
s={10,30,20,46,46,78,39}
print(s)
for a in s:
    print(a)
#set functions
#set add pop remove clear discard update
l=[10,20,40,30,50,60]
s=set(l)
print(s)
s.remove(20)
print(s)
s.discard(50)
print(s)
s.pop() #kuchh bhi apni marzi se delete kardega
print(s)
s.clear()
print(s)
s.add(40)
print(s)
s.update(l)
print(s)
