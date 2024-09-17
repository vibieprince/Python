# 41 Write a program to print whether a given number is prime number or not
"""
n = int(input("Enter the number : "))
flag = False
if n ==1:
    print("1 is not a prime number ")
elif n >1:
    for i in range(2,n):
        if (n % i) ==0:
            flag = True
            break
    if flag:
        print(n,"is not a prime number")
    else:
        print(n,"is a prime number")
"""
### 42 Print all the armstrong numbers in the range 100 to 1000
"""



"""
# 43 The current population of a town is 10000. The population of the town is increasing at the rate of 10% per
# year.You have to write a program to find out the population at the end of each of the last 10 years. For
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on
"""
year = 2023
target = int(input("Enter the year : "))
population = 1000
if (target-year) > 0:
    for i in range(target - year):
        temp = population
        population = population + 0.1*temp
    print("Population in year", target, "is estimated about :", int(population))
else:
    for i in range(year-target):
        temp = population
        population = population - 0.1*temp
    print("Population in year", target, "was :", int(population))
"""
# 44 Write a program to print all the unique combinations of 1,2,3 and 4
"""
for i in range(1,5):
    for j in range (1,5):
        for k in range(1,5):
            for l in range(1,5):
                if (i != j and j != k and k != l and l != i and l != j and i != k):
                    print(i,j,k,l)
"""
# 45 User will provide 2 numbers you have to find the HCF of those 2 numbers
"""
A = int(input("Enter the number A : "))
B = int(input("Enter the number B : "))
HCF = 0
if A>B:
    smaller = B
else:
    smaller = A
for i in range(1,smaller +1):
    if((A % i ==0) and (B % i == 0)):
        HCF = i

print("HCF of",A,"and",B,"is :",HCF)
"""
# 46 Write a program to limit numbers only as a user input
"""
while True:
    p = int(input("Enter the number : "))
    if p == "Exit" or p == "exit" or p == "EXIT":
        exit()
    else:
        pass
    try:
        p = int(input("Enter the number : "))
        print(f'You entered {p}.')
    except Exception as e:
        print("Only numbers are allowed !")
"""
# 47 User will provide 2 numbers you have to find the LCM of those 2 numbers
"""
n = int(input("Enter the number A : "))
m = int(input("Enter the number B : "))

for i in range(max(n,m),1 + (n*m)):
    if i % n == i % m == 0:
        LCM = i
        print("LCM of ",n,"and",m,"is",LCM)
        break
"""
# 48 Print first 25 prime numbers
"""
from math import sqrt
n = int(input("Enter the number : "))
count = 0
k = 2
print("First ",n,"Prime numbers are : ")
while count < n:
    prime = True
    for i in range(2,int(sqrt(k))+1):
        if k % i == 0:
            prime = False
            break
    if prime :
        print(k,end=" ")
        count = count + 1
    k = k +1
"""
# 49 Print first 20 numbers of a Fibonacci Series
"""
n = int(input("Enter the number : "))
j,k = 0,1
count = 0
if n < 0:
    print("Please enter a positive value : ")
elif n == 1:
    print("Fibonacci series upto 1 term is : 0 ")
else:
    print("Fibonacci sequence : ")
    while count < n:
        print(j)
        nth = j + k
        j = k
        k = nth
        count += 1
"""
### 50 Write a program to calculate compound interest
"""
P = float(input("Enter initial Principal Balance (P) : "))
r = float(input("Enter interest rate (r) : "))
n = float(input("Enter number of times interest is compounded (n) : "))
t = float(input("Enter time period (t) : "))
raisetopower = n*t
A = ((n+r)/100*n)**raisetopower
CompoundInterest = (P*A) - P
print(CompoundInterest)
"""
# 51 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""
l=[]
n = int(input("Enter the number : "))
for i in range(1,4):
    s = i*n
    l.append(s)
print(sum(l))
"""
# 52 Take a number from the user and find the number of digits in it.
"""
n = list(input("Enter the number : "))
print("It is a",len(n),"digit number.")
"""
# 53 Print all factors of a given number provided by the user
"""
n = int(input("Enter the number : "))
l=[]
for i in range(1,n):
    if n % i == 0:
        l.append(i)
        #print(i,end="")
print("Factors of",n,"are :",l)
"""
# 54 Find the reverse of a number provided by the user
"""
n = input("Enter the number : ")
print("Reversed number is :",n[::-1])
"""
# 55 Write a program to print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
"""
for i in range(1,6):
    print(i*" *")
"""
# 56 Write a program to print the following pattern
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
"""
for i in range(1,5):
    print(i*" *")

for j in range(5, 0, -1):
    print(j*" *")
"""
# 57 Write a program to print the following pattern
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
# * * * * * * *
"""
space = 6
star = 1
while space >0:
    print(' '*space,end=" ")
    space = space - 1
    for i in range(star):
        print('*',end=" ")
    star = star + 1
    print()
"""
# 58 Write a program to print the following pattern
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
"""
# Code copied from chat gpt ai

def print_pattern(n):
    for i in range(1, n + 1):
        # print numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=" ")
        # Print numbers from i-1 down to 1
        for j in range(i - 1, 0, -1):
            print(j,end=" ")
        print()

print_pattern(5)
"""
# 59 Write a program to print the following pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
"""
def print_pattern(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

print_pattern(4)
"""
# 60 Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! + .....+ n/n!
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def calculate_series_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i/factorial(i)
    return sum

n = int(input("Enter the number of terms upto you want sum : "))
series_sum = calculate_series_sum(n)
print("Sum of the series : {:.2f}".format(series_sum)) #This 2f gives the approximated answer upto 2 decimal places
"""