# Data type 1 - NUMBER
a = 5
print(a,type(a)) #int
a=5.5
print(a,type(a)) #float
a= 5+3j
print(a,type(a)) #complex

#Data type 2 - STRING
s='hello@123'
print(s,type(s))
s= '''      
      hey
      prince this side
      nice to meet you'''
print(s,type(s))
s='10'
print(s,type(s))

#Data type 3 - LIST
L = [1,2,3,'four',5,5.5,6,]
print(L,type(L))
L[2]=5
print(L,type(L))

#Data type 2 - TUPLE
T=(100,34,27,19,45)
print(T,type(T))

#Data type 4 - DICTIONARY
d={"subject name" : 'Mathematcs',
    "Marks" : '45/50'}
print(d,type(d))
print(d['subject name'])

#Data type 5 - SETS
s={10,34,22,18,24,34}
print(s,type(s))


