import keyword
#variables 
#stroing variables
from ast import keyword
from traceback import print_tb


username = "jatuesta@illumina.com"
#printing in the terminal 
print(username)
#printing the type of the variable
print(type(username))

#Variables change and the machine reads the last value as the ultimate value example
x = 200
print (x)

x = 600 
print(x)

#you can store variables in other variables as such
y = x
print(x)

#the variable points at the value that has a specific location and thats how it knows what to print
#to print the location of the values 
print(id(x))
print(id(y)) #the location is the same because it safes memory it points in the same direction saving memory. Only if they have the same value

x= 600
y=900

print(id(x))
print(id(y)) #they know have a different location because they are stored sepetatly
#----------------------------------------------------------------------------------------------------------------------------------------------------
#variable rules in Python
#variable must star with letter or number
#Varibale name cannot start with a number
#Variable name can only contain alpha-numeric characters and underscores
#Variable names are case-sensitive 
#you cannot use the reserverd python names

#Understanding varibales
#rule 1
_test ="Learning Python"
#rule 2
python_test90 = 676
print(_test)
print(python_test90)
#as you can see in the terminal you have no errors and the varibales are being printed. If you where to use a space or a reserved word it would promt an erro
#rule 3 - case sensitive
Daniel = "Daniel"
daniel ="Jorge"
print(Daniel)
print(daniel) # as you can see the out put is different but if we had the same name case sensitve the value that would be safed on that varibale would be Jorge not Daniel. 

#Rule 4- You cannot use reserverd key word
#This are words used by the language and have specific functions attached to it 
#keywordlist = keyword.kwlist
#print(keywordlist)

