a=int(input('Enter the 1st number :- '))
b=int(input('Enter the 2nd number :- '))
n=int(input('''
       1 Addition
       2 Subtraction
       3 Division
       4 Approximate division
       5 Float Division
       6 Percentage 
       7 Multiplication '''))
print()
if n==1:
    print(a+b)
elif n==2:
    print(a-b)
elif n==3:
    print(a/b)
elif n==4:
    print(a%b)
elif n==5:
    print(a//b)
elif n==6:
    print(a/b * 100)
else:
    print('Invalid operation')
print(n)
