#String Slicing
# S[startindex:endindex:step]

from time import process_time_ns


s= "welcome to software testing mentor and rcv academy"

#value of the string at index 0 
print(s[0])
#value at the end of the list
print(s[-1])

#Slice so I want to start at index 0 and end at index 8
print(s[0:8])

#start in the somewhere else than the start index
print(s[4:8])

#you can do step which it means that it will omit that portion 
print(s[0:8:2]) #it should start at cero and the omit the second two positions adn give that value until index 8

""" You can use the index from the begining and at the end if you want to 
get the end values only you can reference the index with a -"""

#if you want to reverse the string you can by using :: and you can even do it by the last index here is how
print(s[::-1]) #this means that the stirng order is now reversed and the letters from each sentence are reversed as well

#if you need to know what is the index to slice you can do that with the function index. You will have to specify the separtor in this case we are using ,

y = 'Name, Age, Address, Country' # you only want the Name here is how you know where to start your slice without counting

print(y.index(',')) #this printed out 4 so we can slice there like this
name = y[0:4]
print(name)

#you could even do it faster by putting it all in the code like this 
name = y[0:y.index(',')] #you need to use this it helps simplify everything
print(name)

#lets practice on getting the other values for y and storing them in their own variables

age = y[5:9]
print(f"this is age:{age}")