import random
n=random.randint(2,5)
print(n)
p=random.randrange(2,5) #5 kabhi include nhi karega
print(p)
l=[4,3,6,78,5,6,4,4]
i=random.choice(l)
print(i)
r=random.random()
print(r)
random.shuffle(l)
print(l)
u=random.uniform(3,0)
print(u)