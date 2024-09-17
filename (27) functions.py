l=[1,2,3,4,5,6,7,8]
del l[2] #index number
print(l)
print(l.pop(4)) #index number

l.remove(7) #value
print(l)

#l.clear()
#print(l)

l[0]=10 #updation
print(l)

print()
l.insert(5,6789876) #insert
print(l)

print()
l.append(70) #append
print(l)
print()
n=[50,60]
l.extend(n)
print(l)
l.insert(3,n)
print(l)