# 61 Write a program that keeps on accepting a number until the user enters 0.Display the sum and average of all the numbers.
"""
l=[]
while True:
    num = int(input('''
                    Enter the number :
                    (press 0 to exit() '''))
    if num == 0:
        break
    l.append(num)

sum = sum(l)
count = len(l)
average = sum/count if count>0 else exit('''

                                         Exiting the terminal...

                                         exited !''')
print()

print("Sum of the numbers is :",sum)
print("Average of the numbers is :",average)
"""
# 62 Write a program to get only integral inputs from the user in a single line
"""
while True:
    try:
        n = input("Enter the numbers separated by spaces : ").split()
        m = [int(numbers) for numbers in n]
        print()
        print("Numbers entered :", m)
        break
    except Exception as e:
        print()
        print("Enter integers only !")
        print()
"""
# 63 Write a program that accepts 2 numbers from the user as numerator and denominator and then simplifies it
"""
numerator = int(input("Enter the numerator : "))
denominator = int(input("Enter the denominator : "))
if numerator > denominator:
    if numerator % denominator == 0:
        sv = int(numerator/denominator)
        print()
        print(f'The simplified value is : {sv}')
    else:
        k = []
        l = []
        for i in range(2, denominator + 1):
            if denominator % i == 0:
                k.append(i)
        for j in range(2, numerator + 1):
            if numerator % j == 0:
                l.append(j)
        # code for program to work for prime numbers too
        if len(l) < 2 or len(k) < 2:
            print()
            print(f'Already the simplified value : {numerator}/{denominator}')
            exit()
        o = []
        for m in l:
            for n in k:
                if m == n:
                    o.append(m)

        if len(o) == 0:
            print()
            print(f"Already the simplified value {numerator}/{denominator}")
            exit()
        else:
            m2 = max(o)
            sn = int(numerator / m2)
            sd = int(denominator / m2)
            print()
            print(f'The simplified value is : {sn}/{sd}')
elif numerator == denominator:
    print()
    print("Simplified value is : 1")
else:
    k = []
    l = []
    for i in range(2,denominator+1):
        if denominator % i == 0:
            k.append(i)
    for j in range(2,numerator+1):
        if numerator % j == 0:
            l.append(j)
    # code for program to work for prime numbers too
    if len(l) < 2 or len(k) < 2:
        print()
        print(f'Already the simplified value : {numerator}/{denominator}')
        exit()
    o = []
    for m in l:
        for n in k:
            if m == n:
                o.append(m)

    if len(o) == 0 :
        print()
        print(f"Already the simplified value {numerator}/{denominator}")
        exit()
    else:
        m2 = max(o)
        sn = int(numerator / m2)
        sd = int(denominator / m2)
        print()
        print(f'The simplified value is : {sn}/{sd}')

# Rental Homes
# Paints
# Marriage
# Digital Marketing
# Artificial Intelligence
# Metals
# IT and Software's company
# Stock Market
"""
# 64 Find the length of a given string without using len() function
"""
count = 0
string = str(input("Enter a string : "))
for i in string:
    count += 1
print("Length of the given string :",count)
"""
# 65 Extract username from the given email
"""
email = input("Enter your email id : ")
f = email.find("@")
if f == -1:
    print("Please enter a valid email ID")
else:
    username = email.split("@")[0]
    print("username :", username)
    p = email.split("@")[-1]
    g = p.find("gmail")
    y = p.find("yahoo")
    if g != -1:
        print("Service provider : Google")
    elif y != -1:
        print("Service provider : Yahoo")
    else:
        print("Enter a valid service provider ")
"""
# 66 Count the frequency of a particular character in a provided string
"""
string = str(input('''
                   Enter a String : '''))
print()
repeat = str(input("Which character you want to count : "))
find = string.count(repeat)
if find == 1:
    print()
    print(f'{repeat} is used only once in the given line(s)')
elif find == 0:
    print()
    print(f'{repeat} is not available in the given line(s)')
else:
    print(f'{repeat} is repeated {find} times in the given line(s)')
"""
# 67 Find the index position of a particular character in another string
"""
string = str(input("Enter the string : "))
print()
index = str(input("Which character's index number you want? :"))
print()
while True:
    try:
        print(f'{index} is placed at index number ',string.index(index),'in the given line(s)')
        exit()
    except Exception as e:
        print(f'{index} not found in the given string!')
        exit()
"""
# 68 Count the number of vowels in a string provided by the user
"""
string = str(input("Enter the string : "))
a = string.count("a")
e = string.count("e")
i = string.count("i")
o = string.count("o")
u = string.count("u")

print("Vowels in given string are appeared",a+e+i+o+u,"times")
"""
# 69 Write a program which can remove a particular character from a string
"""
string = str(input("Enter a string : "))
remove = str(input("Which character you want to remove : "))
print(string.replace(remove,""))
"""
# 69 Write a python programme to remove all the duplicates from a list
"""
nums = input("Enter the numbers separated by spaces : ").split()
mums = [int(numbers) for numbers in nums]
print()
print("We've got from you :",mums)
print()
print("After removing duplicate elements :",set(mums))
"""
# 70 Write a python programme to find the max item from a list without using the max function
"""
def find_max_item(lst):
    if not lst:
        return None
    max_item = lst[0]
    for item in lst:
        if item > max_item:
            max_item = item
    return max_item

#usage
n = input("Enter the number separated by spaces : ").split()
my_list = [int(numbers) for numbers in n]
maximum = find_max_item(my_list)
print(f'The maximum item in the list : {maximum}')
"""
# 71 Write a python programme to convert a string title case without using the title()
"""
def convert_to_title_case(string):
    if not string:
        return ""
    words = string.split()
    title_case_words = []
    for word in words:
        title_case_words = word[0].upper() + word[1:].lower()
        title_case_words.append(title_case_words)
    return " ".join(title_case_words)
#usage
my_string = "hello world"
title_case_string = convert_to_title_case(my_string)
print(f'The title case string is : {title_case_string}')
"""
# 72 Write a python programme to reverse a list
"""
n = input("Enter the number : ").split()
m = [int(numbers) for numbers in n ]
print()
print("We've got from you :",m)
print()
print("Reversed list of given numbers :",m[::-1])
"""
# 73 Write a program to search a given number from a list
"""
num = input("Enter the list of numbers {separated by spaces}: ").split()
mums = [int(numbers) for numbers in num]
find = int(input("Which number you want to find in the given list of numbers : "))
while True:
    try:
        f = mums.index(find)
        print(f'{find} is placed at index number {f} in the given list of numbers.')
        exit()
    except Exception as e:
        print(f'{find} is not found in the given list of numbers')
        exit()
"""
# 74 Write a program that can create a new list from a given list where each item in the new list is square of the item of the old list
"""
list1 = input("Enter the numbers {separated by spaces} : ").split()
list = [int(numbers) for numbers in list1]
l=[]
for i in list:
    j = i**2
    l.append(j)
print("The list with squared numbers from the given numbers :",l)
"""
# 75 Write a program that can revrse words of a given string
"""
#code copied from chatGPT AI
def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string

input_string  = "Hello how are you"
reversed_string = reverse_words(input_string)
print(reversed_string)
"""
# 76 Write a program that can count the number of words in a given string
"""
string = str(input("Enter a string : "))
words = string.split()
count = len(words)
print("The given string has",count,"words")
"""
### 77 Write a program to check if a list is in ascending order or not
"""
list = input("Enter the numbers {separated by spaces} :").split()
mist = [int(numbers) for numbers in list]
for i in range(len(mist)-1):
    if mist[i] > mist[i+1]:
        print("not")
        exit()
    else:
        print("yes")
"""
# 78 Create 2 lists from a given list where 1st list will contain all the odd numbers from the original list and the 2nd one will contain
# all the even numbers
"""
list = input("Enter the numbers {separated by spaces} : ").split()
mist = [int(numbers) for numbers in list]
even = []
odd = []
for i in mist:
    if i % 2 == 0:
       even.append(i)
    else:
        odd.append(i)

print("List of even numbers :",even)
print("List of odd numbers :",odd)
"""
# 79 Write a program to merge 2 lists using the + operator
"""
list1 = input("Enter the numbers {separated by spaces}").split()
list2 = input("Enter the numbers {separated by spaces}").split()
mist1 = [int(numbers) for numbers in list1]
mist2 = [int(numbers) for numbers in list2]
print(mist1+mist2)
"""
# 80 Write a program to replace an item with a different item if found in the list
"""
string = str(input("Enter a string : "))
strin = str(input("Which word you want to replace : "))
f=string.find(strin)
if f == -1:
    print("not found")
else :
    replac = str(input(f'which word you want to place at the place of {strin}'))
    s=string.replace(replac,"")

    print(s)
"""
