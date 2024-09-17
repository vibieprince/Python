w='welcome to wscubetech'
n=w.lower()
print(n)

u=w.upper()
print(u)

t=w.title()
print(t)

x=w.capitalize()
print(x)

print(w.find('e'))
print(w.find('el'))
print(w.find('e',2))
print(w.find('z',2))

print(w.index('e'))

print(w.isalpha())
print(w.isdigit())

w='123'
print(w.isdigit())

w='xyz123'
print(w.isalnum())

w='xyz 123'
print(w.isalnum())

w='xyz@123'
print(w.isalnum())
