# Web-Soft-Tutorials:
from typing import Dict, Union

print('Hello Python World')  # print Hello Python World.

# Variables:
# Variables is use to store data in it.

name = 'Ashfaq'     # string (str)
age = 18            # integer (int)
Salary = 1000.0     # Float  (float)

# Multiples values assign & Print in 1 line:

Ename, Eage, Esalary = 'Ashfaq', 18, 1000.0
print(Ename, Eage, Esalary)

# Multiples Variable assign 1 Value:
ashfaq = afaq = 'Brothers'
# if you type print('ashfaq') or ('afaq') it will print 'Brothers'
# Because we assign 'ashfaq' and 'afaq' so that why its print 'Brothers'
print(afaq)
print(ashfaq)

# Data types in Python:
# 1)Numbers
# 2)String
# 3)List
# 4)Tuple
# 5)Dictionary

# To Check Data Type:
Age = 18            # integer (int)
salary = 1000.0     # Float  (float)
print(type(age))
print(type(salary))
print(type(name))

# Numbers:
# Perform Arithmetic Operations

value0 = 6
value1 = 4

# Addition: +
resultAdd = value0 + value1
print(resultAdd)

# Subtract: -
resultSub = value0 - value1
print(resultSub)

# Multiply: *
resultMul = value0 * value1
print(resultMul)

# Divide: /
resultDiv = value0 / value1
print(resultDiv)

# Reminder: %
resultRem = value0 % value1
print(resultRem)

# Convert Data Type:
print(salary)       # simply type int(salary) to convert in 'integer'
print(age)          # simply type float(age) to convert in 'float'

# Strings:
# print Index
name = 'Ashfaq Ahmed'
# Example 1:
print(name[0])
# its print first letter 'A' because machine language run code left to right ( 0 to end )
# so its prints 'A'

# Slicing:~

# Example 2:
print(name[5])
# Now its prints Index on fifth Index of name
# so its print 'q'

# Example 3:
# if you want to print 0 to 3
print(name[0:3])
# so its print (0 to 2) 'A' To 'h' and leaves 3rd one
# its mean every time you use index like [0:3] it decrement last one number whether its 'number' ot 'alphabet'

# Example 4:
# if you want print Blank 'Space' Between 'Ashfaq '' Ahmed'
print(name[0:6])
# its starts 'A' mean 0 To 'Blank Space' 6
# so its print 0 to 5 it leave blank space

# Finding: in
# Example 1:
# Spouse if you want to find a 'Number' or 'Alphabet' just type
print('A' in name)
# its print 'True' Other wise 'False'
# Example 2:
# Find 'Name' type
print('Ahmed' in name)
# its print 'True' Otherwise 'False'

# Concatenate Values:~
concatenate = 'Ashfaq'+' '+'Ahmed'      # In the center is for space ' '.
print(concatenate)

# Concatenate Variables:~
cona = 'Ashfaq'
conb = ' '              # In the center is for space ' '.
conc = 'Ahmed'
cont = cona + conb + conc
print(cont)

# Concatenate String With Integer:~
conage = 18                    # if Concatenate string with number then first convert conage
print(cona + str(conage))      # into string by simply type str(conage) then its convert otherwise error!!


# List:~
# List Work Like Arrays means one variables stores multiple values.
# Every Values is store in it, its on particular Index.
# its store data of every Type ,whether its (str , in , float) etc.

students = ['ashfaq', 'safdar', 'irfan', 'saim', 'zain']      # List Must be in Square Brackets
print(students[0])     # to print 0 index from the list 'student'
print(students[2])     # it will print thr third index from th list.

# To Add a Name in the list Using 'append' function:~
students.append('adnan')        # name will add in 'students' list.
print(students)

# To change Name Or update the name:~
students[0] = 'ash'
print(students)

# Same Name in the list using 'append' Function:~
students.append('irfan')
print(students)

# To Count The Same Name in List using 'count' function:~
print(students.count('irfan'))

# To Remove an Name like irfan:~
students.remove('irfan')
print(students)         # it will remove the first on because Codes Rub left to right.

# To Sort list in Alphabetic:
students.sort()     # its sort in alphabetical wise 'A to Z'.
print(students)

# To Reverse Sorting:~
students.reverse()         # its sort in reverse alphabetical wise 'Z to A'.
print(students)

# To Concatenate list:~
students2 = ['ali', 'sami']         # concatenate two list
studentst = students + students2
print(studentst)

# To Find Maximum and Minimum marks in list:~
marks = [44, 55, 66, 77, 88]
print(max(marks), 'Maximum Marks')   # for maximum (highest) marks type max(variable name).
print(min(marks), 'Minimum Marks')   # for minimum (lowest) marks type min(variable name).

# Remove List:~
del studentst
# it will not show the list because the list was deleted.


# Dictionary:~
# in Dictionary we have a key and its value.
# to access value we use its key.
studic = {'Name': 'Ashfaq', 'Age': 18}  # so 'Name' is the key & 'Ashfaq' is Value.
print(studic)                           # ':' sami colon is must to identify its a key.

# Suppose to Check Name in Dictionary 'studic' , Simply Type
print(studic ['Name'])

# To Update Data In Dictionary:
studic['Age'] = 19
print(studic['Age'])

# To Add Data in Dictionary:
studic ['Gender'] = 'Male'
print(studic['Gender'])

# To Delete a Key:
del studic['Gender']
print(studic)

# To Find the Length:
# Means How Many Elements are there in it.
print(len(studic)) # so the Elements are the Keys , there are 2 keys.

# To Check the type:
print(type(studic))

# To check keys in Dictionary that created Above:
print(studic.keys())

# To Check Values in Dictionary that created Above:
print(studic.values())

# Add Data to the first Dictionary 'studic'.
# first create second Dictionary.
studic1 = { 'RollNo': 75459, 'Country': 'Pakistan'}
print(studic1)
# Now
studic.update(studic1)
print(studic)

# To Clear a Dictionary:
studic.clear()
print(studic)

# To Delete a Dictionary:
del studic          # So its Completely deleted

# Tuples:~
# Tuples are just like a lists buy they are immutable objects means you can't change its values.it will remain same.

# Make Tuple
tuple = ('Ashfaq', 'Safdar', 'Irfan', 1, 2, 3)
print(tuple)

# To Access Tuple
print(tuple[1])       # to access tuple you want to type tuple[] with square brackets

# Slicing in tuple
print(tuple[0:2])
print(tuple[1:])

# To Find length in tuple
print(len(tuple))      # so there is 6 element in 'tuple'

# "Basic Functions":

# Concatenate tuples
# first create second tuple to concatenate.
tuple1 = (1, 2, 3, 4, 5, 6)
print(tuple1)
# Now
tuple0 = tuple + tuple1
print(tuple0)

# it can repeative
print(tuple * 2)          # its print tuple 2 times

# Find a value in tuple
print(5 in tuple1)

# To find Maximum & Minimum No.
print(max(tuple1))  # its show the Maximum No. in 'tuple1'
print(min(tuple1))  # its show the Minimum No. in 'tuple1'

# To delete tuple
del tuple

print(tuple)