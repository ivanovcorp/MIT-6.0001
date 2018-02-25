# variables
from _ast import For
from _operator import index
a = 5 # int
print('This is int:',a)

b = 6.2 # float
print('This is float:',b)

s = 'I am a string' # string
print('This is string:',s)

amGood = True # boolean
print('This is boolean:',amGood)

amSick = False # boolean
print('This is also a boolean:',amSick)

# if - else
if a < b:
    print("This is the if: a < b")
    
if a > b:
    a += 1
else:
    print('This is the else: a < b')    
    
today = 'Monday'    
if today == 'Tuesday':
    print('This is if. Today is Tuesday')
elif today == 'Monday':
    print('This is elif(else if). Today is', today)
else:
    print('This is else. We don\'t know what day it is today.')
    
# while loop
num = 0
print('Before while loop, num is:',num)
while num < 5:
    num += 1
print('After the while loop num is:', num)

# for loop
result = ''
for i in range(0, 10, 2):
    result += str(i)
print('After the for loop this is the result:',result)

# string indexation
indexedString = 'Ivan'
print(indexedString[0:4]) 
print(indexedString[::-1]) # reversed string

# functions
def funcWithReturn(num1, num2):
    return num1 + num2
print('This is the result of funcWithReturn(5,5):',funcWithReturn(5, 5))

def funcWithoutReturn(num1, num2):
    print('This is printed from funcWithoutReturn. The result of :',num1,'+',num2, '=', (num1 + num2))
funcWithoutReturn(6, 5) 

# tuples
te = (5, 'ivan', 2.2)
for i in te:
    print(i)
print('Lenght of the tuple is:', len(te))

print('Slice tuple from 1 to 2', te[1:2])
print('Slice tuple from 1 to 3', te[0:3])
print('Slice tuple from 0 to 2', te[0:2])

# lists
L = [2, 'a', 3, [0, 1]]
for i in L:
    print('Element:', i)
print('Size of the list is:', len(L))
print('Element L[1] before change:', L[1])
L[1] = 'b'
print('Element L[1] after change:', L[1])
print('Adding element to the lis: 155')
L.append(155)
for i in L:
    print('Element:', i)
print('Removing element 155.')
L.remove(155)
for i in L:
    print('Element:', i)
L1 = [1, 2, 3]
L2 = [4, 5, 6]
LF = L1 + L2
for i in LF:
    print('Element:', i)
print('Remove last elem and get its value:',LF.pop())
for i in LF:
    print('Element:', i)
print('Printing list after removing value at [0]')
del(LF[0])
for i in LF:
    print('Element:', i)
str1 = 'Convert me to list'
L3 = list(str1)
for i in L3:
    print('Element:', i)
str2 = '5 < 6 ha ha'
print('Before split:', str2)
L4 = str2.split('<')
for i in L4:
    print('Element:', i)
L5 = ['a', 'b', 'c']
print('Joining L5 to string:', ''.join(L5))
L6 = [9, 6, 0, 3]
print('Sorted:', sorted(L6))
print('The list is not changed after calling sorted:', L6)
L6.sort()
print('However when calling sort funct. the list is sorted:',L6)

# aliases

warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink')
print('hot:', hot)
print('warm:', warm)

# clone
cool = ['blue', 'green', 'grey']
chill = cool[:]
chill.append('black')
print('chill:', chill)
print('cool:'   , cool)

# Recursion
def mult(a, b):
    if b == 1:
        return a
    else :
        return a + mult(a, b - 1)
    
print(mult(6, 4))

def fact(n):
    if n == 1:
        return 1
    else :
        return n * fact(n - 1)
print(fact(10))

def fib(x):
    if x == 0 or x == 1:
        return 1
    else :
        return fib(x - 1) + fib(x - 2)
print(fib(4))

# dictionary
my_dict = {}
grades = {'Ivan' : 6, 'Pesho' : 3, 'Gosho' : 2}
print('All grades:', grades)
print('Ivan:', grades['Ivan'])
grades['Tosho'] = 5
print('Added grade for Tosho:', grades)
print('Is Ivan in the dictionary:', 'Ivan' in grades)
del(grades['Tosho'])
print('Deleted Tosho:', grades)
print('All keys:', grades.keys())
print('All keys:', grades.values())