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
    