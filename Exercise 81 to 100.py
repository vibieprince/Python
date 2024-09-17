### 81 Write a program to convert a 2D list to 1D list
"""
def convert(list2d):
    list1d = []
    for sublist in list2d:
        list1d.extend(sublist)
    return list1d

def print(list):
    for item in list:
        print(item)

twoD = []
oneD = convert(twoD)
print(oneD)
"""
# 82 Write a program that can perform union and intersection on 2 two given list
"""
list1 = input("Enter the numbers separated by spaces : ").split()
list2 = input("Enter the numbers separated by spaces : ").split()
mist1 = [int(numbers) for numbers in list1]
mist2 = [int(numbers) for numbers in list2]
print()
print("Union of lists :",mist1+mist2)
l=[]
for num in mist1:
    for gum in mist2:
        if num == gum:
            l.append(num)
print()
print("Intersection of lists :",l)
"""
# 83 Find the max item of each row of a matrix
"""
def find_max(matrix):
    max_values = []
    for row in matrix:
        max_value = max(row)
        max_values.append(max_value)
    return max_values

matrix = [
    [4,5,6],
    [8,9,10],
    [11,45,13]
]

result = find_max(matrix)
print(result)
"""
# 84 Write a program to convert a integer to string
"""
def inttostring(num):
    if num == 0:
        return '0'
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)
    result = ' '
    while num > 0:
        digit = num % 10
        result = str(digit) + result
        num = num // 10
    if is_negative:
        result = '-' + result
    return result

number = int(input("Enter A integer : "))
result_string = inttostring(number)
print("Converted string :",result_string)
"""
# 86 Write a program that can print the shape of a matrix
"""
def shape(matrix):
    rows = len(matrix)
    columns = len(matrix[0]) if matrix else 0
    print("Matrix shape : {} X {}".format(rows,columns))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
shape(matrix)
"""
# 87 Write a program that can check if you can perform matrix multiplication on 2 matrices
"""
def matrices(matrix1,matrix2):
    rowws1 = len(matrix1)
    columns1 = len(matrix1[0]) if matrix1 else 0
    rows2 = len(matrix2)
    columns2 = len(matrix2[0]) if matrix2 else 0
    
    if columns1 == rows2:
        return True
    else:
        return False
    
matrix1 = [[1,2,3],[3,4,5]]
matrix2 = [[3,6,4],[4,5,7],[4,8,2]]

if matrices(matrix1,matrix2):
    print("multiplication is possible")
else:
    print("Multplication can't be possible ")
"""
# 88 Write a program that can sort a given unsorted list.Don't use any built in function for sorting.
"""
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        #Last i elements are already in place
        for j in range(0,n-i-1):
            #Transverse the array from 0 to n-i-1
            #swap if the element found is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

#Example usage
unsorted_list = [64,34,25,12,22,11,90]
print("Unsorted List :",unsorted_list)
bubble_sort(unsorted_list)
print()
print("Sorted List :",unsorted_list)
"""
# 89 Write a program that can find the most used word in a bollywood song
"""
from collections import Counter
def mostusedword(song):
    cleaned = ''.join(c.lower() if c.isalnum() else ' ' for c in song)
    words = cleaned.split()
    words_count = Counter(words)
    mostcommon,count = words_count.most_common(1)[0]
    return mostcommon,count

#Example usage
song = '''
Dilbar,dilbar,haan dilbar
Dilbar,dilbar,haan dilbar
'''
mostcommon,count = mostusedword(song)
print(f"The most used word is {mostcommon} with a count of {count}.")
"""
# 90 Write a program to perform matrix multiplication on 2 matrices
"""
def matrixmultiplication(matrix1,matrix2):
    row1 = len(matrix1)
    row2 = len(matrix2)
    col1 = len(matrix1[0])
    col2 = len(matrix2[0])

    if col1 != row2:
        print("Matrix multiplication not possible !")
        return None
    result = [[0 for i in range(col2)] for i in range(row1)]
    for j in range(row1):
        for k in range(col2):
            for m in range(col1):
                result[j][k] += matrix1[j][m] * matrix2[m][k]
    return result

#Example usage
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[7,8],[9,10],[11,12]]

result = matrixmultiplication(matrix1,matrix2)
if result is not None:
    print("Matrix multiplication result : ")
    for row in result:
        print(row)
"""
# 91 Assume a list with numbers from 1 to 10 and then convert it into a dictionary where the key would be the numbers of the list
# and values will be the squares of those numbers
"""
numbers_list = list(range(1,11))
numbers_dict = {num ** 2 for num in numbers_list}
print(sorted(numbers_dict))
"""
# 92 Write a program to merge two given dictionary
"""
def merge_dicts(dict1,dict2):
    merge_dict = dict1.copy() #create a copy of dict1 to preserve its original content
    merge_dict.update(dict2) #update the copy with the key-value pairs from dict2
    return merge_dict

#Example usage
dict1 = {'a':1,'b': 2}
dict2 = {'c':3,'d': 4}

merge_dict = merge_dicts(dict1,dict2)
print(merge_dict)
"""
# 93 write a program to swap the key value pairs for max and min values
# Eg if the dict is like this
# {'a':1,'b':2,'c':3}
# Output should be {a:3,b:2,c:1}
"""
def swap_max_min(dictionary):
    if not dictionary:
        return dictionary

    max_key = max(dictionary,key=dictionary.get)
    min_key = min(dictionary,key=dictionary.get)

    #swap the key-value pairs
    dictionary[max_key],dictionary[min_key] = dictionary[min_key],dictionary[max_key]

    return dictionary

#Example usage
my_dict = {'a':1,'b':2,'c':3}
swapped_dict = swap_max_min(my_dict)
print(swapped_dict)
"""
# 94 Write a program to find histogram of a given set of numbers. Take bin size from user. Print the result in the form of a dictionary.
"""
def caculate_histogram(numbers,bin_size):
    histogram = []

    for num in numbers:
        bin_index = num // bin_size

        if bin_index in histogram:
            histogram[bin_index] += 1
        else:
            histogram[bin_index] = 1

    return histogram

#Example usage
number_list  = [5,10,15,20,25,30,35,40,45,50]
bin_size = int(input("Enter the bin size: "))

histogram_dict = caculate_histogram(number_list,bin_size)
print(histogram_dict)
"""
# 95 Write a function that accepts a string and returns the number of upper case chars and lower case chars as a dictionary
"""
def countchars(string):
    count = {"uppercase": 0,"lowercase":0}

    for char in string:
        if char.isupper():
            count["uppercase"] += 1
        elif char.islower():
            count["lowercase"] += 1

    return count

input_string = "Hello World"
result = countchars(input_string)
print(result)
"""
# 96 Write a function that accepts a list of strings and performs Bag of words and convert it to numerical vectors.
from sklearn.feature_extraction.text import CounVectorizer
