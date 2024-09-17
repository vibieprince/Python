w="welcome {} to {} india".format("hello",20)
print(w)


w="welcome {1} to {0} india".format('hello',20)
print(w)

w='Welcome {a} to {b} india'.format(a='hello',b=20)
print(w)

w='welcome {a:10} to {b} india'.format(a=44,b=20)
print(w)

w='welcome {a:^10} to {b:<10} india'.format(a=44,b=20)
print(w)
