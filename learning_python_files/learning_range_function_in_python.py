#Learning Range functions in python 
# Range is bult in function it generates the sequence of numbers
#Additional doc: https://docs.python.org/3/library/stdtypes.html#typesseq
#Here is the official documentation: https://docs.python.org/3/library/functions.html#func-range
"""
class range(stop)
class range(start, stop[, step])
Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range."""

#Old way of doing it
list_demo = [1,2,3,4,5,6,7,8,9,10]

#Print using for loop
for number in list_demo:
    print(number)

#New way using range function 

for number in range(10):
    print(number) #No need to create a list.

#You can specifiy the start, stop and step 

for number in range(1,11,2):
    print(number) #No need to create a list.

# I will create a list of 1 to 100 using range function 
range_list= []

for number in range(1,101):
    range_list.append(number)
print(range_list)