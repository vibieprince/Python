#Dictionary works on the pair of key and value
#creating dictionary
d={'name' : 'python',
   'fees' : 8000,
   'Duration' : '2 months'
   }

print(type(d))
f=d['fees']
print(f)

for n in d:
    print(n)
    print(d[n])