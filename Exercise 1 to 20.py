# 1 Calculate the multiplication and sum of two numbers
"""
i = int(input("Enter the number A : "))
j = int(input("Enter the number B : "))

p = int(input ('''
      What do you want to do (type integral value)
      1 Multiplication
      2 Addition
      
      '''))

if p == 1:
    print("The multiplication of ",i,"and ",j,"is",i*j)
elif p == 2:
    print("The addition of ",i,"and",j,"is",i+j)
else :
    print("INVALID OPERATION")
"""
# 2 Given two integer numbers return their product only if the product is equal to or lower than 1000,else return their sum.
"""
a = int(input("Enter the number A : "))
b = int(input("Enter the number B : "))

if a*b <= 1000:
    print("The product of",a, "and",b,"is :",a*b)
elif a*b >= 1000:
    print("The addition of",a, "and",b,"is :",a+b)
else:
    print("INVALID OPERATION")
"""
# 3 Write a program to iterate the first 10 numbers and in each iteration,print the sum of the current and previous number.
"""
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for i in range(1,11):
    sum = previous_num+i
    print("Current number",i,"Previous number",previous_num,"| sum :",sum)
    previous_num = i
"""
# 4 Write a program to accept a string from the user and display characters that are present at an even index number.
"""
i = str(input("Enter the word :"))
print("Original word we've got is",i)
p=len(i)
for k in range(0,p-1,2):
    print("index[",k,"]",i[k])


#Alternating way

word = input("Enter the word :")
print("Original String :",word)
print("Printing the characters of even indexes")
x = list(word)
for i in x[0::2]:
    print(i)
"""
# 5 Write a program to remove characters from a string from zero up to n and return a new string.
"""
String = input("Enter the word : ")
l=len(String)
n = int(input('''Enter the index number upto 
                 which you want to remove the 
                 characters from the String
                 : '''))


print("Printing the residual string : ",String[n:])
"""
# 6 Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
"""
numX = [10,20,30,40,50,60,70]
numY = [75,83,58,45,69,28,70]

p = numY[0]
o = numY[-1]

if p==o:
    print("True")
else :
    print("False")

k = numX[0]
j = numX[-1]

if k == j:
    print("True")

else :
    print("False")
"""
# 7 Iterate the given list of numbers and print only those numbers which are divisible by 5
"""
l=[]
for i in range(1,6):
    n = int(input("Enter the value "+str(i)+":"))
    l.append(n)

for num in l:
    if num % 5 == 0:
        print("The numbers that are divisible by 5 are ",num)
"""
# 8 Write a program to find the number of times a word been repeated in a individual line or paragraph
"""
s = str(input("Enter the line(s) : "))
k=s.count("Prince")
print("Prince in this line is appeared ",k,"times")
"""
# 9 PRINT THE FOLLOWING PATTERN
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
"""
for i in range(0,6):
    for p in range(i):
        print(i,end=" ")
    print("\n")
"""
# 10 Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. For example 545,is a palindrome numbers
"""
num = int(input("Enter the number : "))
rev = 0
temp = num
while temp>0:
    rem = temp %10
    rev = (rev*10) + rem
    temp = temp // 10
if num == rev:
    print(num,"is a palindrome.")
else:
    print(num,"is not a palindrome.")
"""
# 11 Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers
#from the first list and even numbers from the second list.
"""
l=[]
for i in range(1,6):
    n = int(input("Enter the value "+str(i)+": "))
    l.append(n)

print()

l1 = []
for i in range(1,6):
    n = int(input("Enter the value "+str(i)+": "))
    l1.append(n)

print()

print("list 1 :",l)
print()
print("list 2 :",l1)

def merge(l,l1):
   l3=[]
   for num in l:
       if num%2 !=0:
          l3.append(num)

   for num in l1:
        if num%2 == 0:
           l3.append(num)
   return l3

print()
print("Taking odd values from list 1"
      " and even values from list 2")
print()
print("Resulting list : ",merge(l,l1))
"""
# 12 Write a program to extract each digit from an integer in the reverse order.
"""
n = int(input("Enter the number : "))
while n > 0:
    digit = n % 10
    n = n // 10
    print(digit,end=" ")
"""
# 13 Calculate income tax for the given income by adhering to the below rules
# first $ 10,000 - 0%
# next $ 10,000 - 10%
# the remaining - 20%
"""
n = int(input("Enter your annual income : "))
if n < 10000:
    tax = 0
elif n <= 20000:
    x = n - 10000
    tax = x * 10/100
else :
    tax = 0
    tax += 10000 *  10/100
    tax += (n - 20000) * 20 / 100

print("Toatal tax payable is Rs.",tax)
"""
# 14 Print multiplication table from 1 TO 10
"""
a = int(input('''Enter the number whose 
multiplication table you want
(1-10) : 
'''))
for i in range(1,11):
    print(a*i,end=" ")
"""
# 15 Print downward half-pyramid pattern with star (asterisk)
"""
a = "*"
for i in range(6,0,-1):
    for j in range(0,i-1):
        print(a,end=' ')
    print(" ")
"""
# 16 Write a function called exponent(base,exp) that returns an int value of base raises to the power of exp.
#Note here exp is a non-negative integer,and the base is an integer.
"""
def exponent(base,exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base,"raises to the power of",exp,"is :",result)

exponent(5,4)
"""
# 17 User will input 3 ages , find the oldest one
"""
l = []
for i in range(1,4):
    n = int(input("Enter your age "+str(i)+": "))
    l.append(n)
print()
m = max(l)
print("The oldest age is ",m)
"""
# 18 Write a program that will convert celsius value to fahreneit
"""
c = int(input("Enter the temperature : "))
F = (9/5)*c + 32
print("Temperature we've received",c,"degree celsius")
print("Temperature in Fahrenheit :",F)
"""
# 19 User will input 2 numbers. Write a program to swap the numbers
"""
num = int(input("Enter the number 1 : "))
num1 = int(input("Enter the number 2 : "))

p = num
num = num1
num1 = p
print()
print("number 1 after swapping :",num)
print("number 2 after swapping :",num1)
"""
# 20 Write a program that will give you the sum of 3 digits
"""
l = []
for i in range(1,4):
    n = int(input("enter the number "+str(i)+": "))
    l.append(n)
print("Total :",sum(l))
"""