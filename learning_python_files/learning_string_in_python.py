#Strings

from calendar import c


x = "This is a string"

y = 'This is also a string'

#Indexing is important the first character has an index of 0 
#so if we want to print only one letter we can do so in this case I want to print the t

print(x[1])
#The [] give us the index of what we want to print

x = "This 'is' a string"

y = 'This is also a string'

print(x)
print(y) #If you have quatation marks iside a string its treated as a quation bot a string just as long as it has a beggining and an end

#you can defgine a multui line comment on python but you need to add it to a varibale if not it will be considered as a multi line comment

t ="""I can print 
This multilne
Comment as a string 
Look at this"""
print(t)

#using membership operators to find if a string is inside a variable strings 
#we are going to check if the word at is in t 
print("at" in t)
#lets look for a word that is not in t like clockwise
print("clock" in t)

# lets check if its case sensitve with the word At
print("At" in t) # IT IS SO BE CAREFUL WHEN LOOKING UP WORDS THERE IS A WAY TO TELL PYTHON TO OVERLOOK CAPITALZIATION BUT MORE OF THAT TO COME
