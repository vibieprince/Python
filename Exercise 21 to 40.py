# 21 Write a program that will reverse a four digit number and also checks if the reverse is true
"""
n = input("Enter the four digit number : ")
l=len(n)
if l == 4:
    k = print(n[::-1])
    if k == n :
        print("Reverse is True, and the given number is a palindrome! ")
    else:
        print("Reverse is not true, and the given numbre is not palindrome")
else:
    print("Please provide a 4 digit number only! ")
"""
# 22 Write a program that will tell whether the number entered by the  user is odd or even
"""
n = int(input("Enter a number : "))
if n % 2==0:
    print(n,"is a even number ")
else :
    print(n,"is an odd number")
"""
# 23 Write a program that will tell whether the given year is leap or not
"""
y = int(input("Enter the number : "))
if y % 400 == 0 and y % 100 ==0:
    print(y,"is a leap year")
elif y% 4==0 and y % 100 != 0:
    print(y,"is a leap year ")
else :
    print(y,"is not a leap year")
"""
###24 Write a program to find Euclids distance between two coordinates
"""
import math

p = list(input("Enter the coordinate (x1,y1,z1) : "))
x1=p[0]
y1=p[1]
z1=p[2]

q = list(input("Enter the coordinate (x2,y2,z2) : "))
x2 = q[0]
y2 = q[1]
z2 = q[2]

f = (x2)-(x1)
#d = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print(f)
"""
# 25 write a program that take a user input of three angles and will find out whether it can form a triangle or not
"""
l = []
for i in range(1,4):
    n = int(input("Enter the angle "+str(i)+" : "))
    l.append(n)
print()
p = sum(l)
print("Total :",p)
print()
if p == 180:
    print("Yes it can form a trangle. ")
else:
    print("No, triangle can't be formed ! ")
"""
# 26 Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
"""
c = int(input("Enter the cost price : "))
s = int(input("Enter the selling price : "))

print()
if c > s:
    print("Its a loss of Rs. ",(c-s))
elif c == s:
    print("Neither a loss nor a profit!")
else :
    print("You had a profit of Rs. ",(s-c))
"""
# 27 Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
"""
p = int(input("Enter the Principle amount : "))
r = int(input("Enter the Rate of interest : "))
t = int(input("Enter the time period : "))

si = p*r*t
k = si/100
print("Simple interest is Rs. :",k)
"""
# 28 Write a program to find the volume of a cylinder. Also fnd the cost when the cost of 1 litre milk is 40Rs.
"""
import math
r = float(input("Enter the radius of cylinder (m) :"))
h = float(input("Enter the height of cylinder (m) :"))

v = math.pi * r*r * h
m = v * 40
print("Volume of the cylinder :",v,"litres")
print()
print("The cost of milk is Rs. ",m)
"""
# 29 Write a program that will tell whether the number is divisible by 3 and 6
"""
n = int(input("Enter the number : "))
if n % 3 ==0 and n % 6 == 0:
    print(n, "is divisible by 3 and 6 both ")
elif n%3 == 0 and n%6 != 0:
    print(n,"is divisible by 3 only")
elif n%3 != 0 and n %6 ==0:
    print(n,"is divisible by 6 only")
else :
    print(n,"is neither divisible by 3 nor by 6")
"""
# 30 write a program to calculate the angle between hour hand and minute hand
"""
H = int(input("Enter the time in hour only {1-12} : "))
M = int(input("Enter the time in minute only {1-60} : "))

print()
if H > 12:
    print("Please enter a valid input in hour hand")
    exit()
elif M > 60:
    print("Please enter a valid input in minute hand ")
    exit()
else :
    pass
print()
HA = H*30
MA = 6 * M

angle = abs(HA-MA)
angle = min(360-angle,angle)

print("The angle between Hour and minute hand is : ",angle,"degree")
"""
### 31 Given two rectangles, fnd if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two
# points:the left top corner of the rectangle . Two rectangles sharing a side are considered overlapping.(L1 and R1 are the extreme points
# of the rectangle and L2 and R2 are extreme points of the second rectangle)
"""


"""
### 32 Write a program that will determine weather when the value of temperature and humidity is provided by the user.
"""
t = str(input("Enter the temperature : "))
p = ascii(F)
if t[-1] == ascii(70):
    print("yes ")
else:
    pass
print(p)
"""
# 33 Write a pyhton program that will take 3 numbers from user as a input and sum their squares
"""
l=[]
p=[]
for i in range(1,4):
    n = int(input("Enter the number "+str(i)+" : "))
    l.append(n)

    for j in range(1):
        k = (n**2)

        print("Square : ",k)
        print()
        p.append(k)


s = sum(p)
print("Sum of squares",s)
"""
### 34 Write a program that will check whether the number is armstrong number or not
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0,1,153,370,407 etc.
"""
l=[]
n = list(input("Enter the number : "))
l.append(n)
for l in range(3):
    print(l)
"""
### 35 Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.
"""



"""
# 36 Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%),and tax(if salary is between 5 - 10lakh = 10%),
# (11-20lakh = 20%),(20-30lakh=30%)
"""
s = int(input("Enter your Salary : "))
print()
HRA = s*(10/100)
print("HRA deducted :",HRA)
print()
DA = s*(5/100)
print("DA deducted :",DA)
print()
PF = s*(3/100)
print("PF deducted :",PF)
print()
tax = 0
if s < 500000:
    print("No taxes to pay! ")
if 500000 <= s <= 1000000:
    k = s - 500000
    tax = tax + 0.1*k
if 1000000 < s < 2000000:
    k = s-1000000
    tax = tax + 50000 + 0.2*k
if 2000000 < s < 3000000:
    k = s - 2000000
    tax = tax + 2000000 + 0.3*k
elif s > 3000000 :
    k = s - 3000000
    tax = tax + 550000 + 0*k

print("Total tax payable :",tax)
print()
print("Salary in hand : ",s-tax)
"""
# 37 Write a menu driven program 1. cm to m | 2. km to miles | 3. USD to INR | 4. exit
"""
n = int(input('''
1. centimetre to metre
2. Kilometres to Miles 
3. USD to INR 
4. Exit 

: '''))

if n == 1:
    c = int(input("Enter the length in centimetres : "))
    print("Length in metres :",c/100,"m")
elif n == 2:
    k = int(input("Enter the length in Kilometres : "))
    print("length in miles : ",k*0.6214,"M")
elif n == 3:
    u = int(input("Enter the $ : "))
    print("Money in INR :","Rs.",u*82.403,)
elif n == 4:
    exit()
else :
    print("Choose a valid input ")
"""
# 38 Write a program to find the sum of first n numbers, where n will be provided by the user.Eg if the user will provide n=10
# the output should be 55
"""
l=[]
n = int(input("Enter the number upto which you want sum : "))
for i in range(1,n+1):
    l.append(i)
s=sum(l)
print("Sum upto",n,"is :",s)
"""
#  39 Write a program that can find the factorial of a given number provided by the user.
"""
factorial = 1
n = int(input("Enter the number whose factorial you want : "))
for i in range(1,n+1):
    factorial = factorial*i

print("The factorial of",n,"is :",factorial)
"""
# 40 Write a program to get first 25 odd numbers
"""
for i in range(50):
    if i%2 != 0:
        print(i)
"""
