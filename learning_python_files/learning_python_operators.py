# Operators

# arithmetic operators
from ast import IsNot
from curses import use_default_colors
from operator import is_not

from pyparsing import And



x = 15
y = 4
#Addition
print(x+y)
#Substraction
print(x-y)
#Multiplication
print(x*y)
#Division
print(x/y)
#Modelular operatro = Remainder
print(x%y)
#To the power of Exponential
print(x**y)
#floor division = return result to nearesth whole number
print(x//y)

# Assignment operators
# the = assings a value
x = 10
# You can different assigment of operators reducing the amount of variables used
#Long way
x = 10 + 2
print(x)
#short way of adding to the value 
x += 2
print(x)

#short way of all operators
x -= 2
print(x)
x /= 2
print(x)
x *= 2
print(x)
x **= 2
print(x)
x %= 2
print(x)
x //= 2
print(x)

# Comparison Operators
#compare the values the return will be a boolena true or false 

x=10
y=6

print(x==y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
#not equal 
print(x!=y)

# Logical Operators
#Two conditional statemnts AND OR NOT

x = 10
y = 4
#when you use AND the both statments need to be true for the return to = true if one of them is not then it will return false
print(x == y and x > y)
#For the OR statment only one has to be true for the return value = true 
print(x == y or x > y)

#you can use any comparison or assignment operators 

# Identity Operators
# IS or ISNOT
#This compares the object not the contents 
x = ["Daniel","Atuesta"]
y = ["Daniel","Atuesta"]

print(x is y)
print( x is not y )

# Membership Operators
#wheater the value in the list is in the other list
x = ["Daniel","Atuesta"]
y = ["Daniel","Atuesta"]
print("Daniel" in y)
print("Daniel" not in y)

# Bitwise Operators
#The work on binary digits
# This are the symbols used
# &- AND
# | OR
# ~ NOT
# ^ XOR
x = 1
y = 3
print( x | y )